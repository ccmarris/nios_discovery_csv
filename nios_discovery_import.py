#!/usr/bin/env python3
#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
'''

 Description:

    Infoblox NIOS Discovery CSV Import

 Requirements:
   Python 3.8+

 Author: Chris Marrison

 Date Last Updated: 20240426

 Todo:

 Copyright (c) 2024 Chris Marrison / Infoblox

 Redistribution and use in source and binary forms,
 with or without modification, are permitted provided
 that the following conditions are met:

 1. Redistributions of source code must retain the above copyright
 notice, this list of conditions and the following disclaimer.

 2. Redistributions in binary form must reproduce the above copyright
 notice, this list of conditions and the following disclaimer in the
 documentation and/or other materials provided with the distribution.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

'''
__version__ = '0.0.2'
__author__ = 'Chris Marrison'
__author_email__ = 'chris@infoblox.com'

import logging
import os
import sys
import requests
import argparse
import configparser
import datetime
import time


def parseargs():
    '''
    Parse Arguments Using argparse

    Parameters:
        None

    Returns:
        Returns parsed arguments
    '''
    parse = argparse.ArgumentParser(description='NIOS Import Discovery Metadata')
    parse.add_argument('-c', '--config', type=str, default='gm.ini',
                        help="Override ini file")
    parse.add_argument('-f', '--file', type=str, default='csv_data.csv',
                        help="Override csv import file")
    parse.add_argument('-v', '--view', type=str, 
                        help="Network View", default='default')
    parse.add_argument('-a', '--action', type=str, 
                        help="Change default action of INSERT (e.g. DELETE) for CSV Import")
    parse.add_argument('-d', '--debug', action='store_true', 
                        help="Enable debug messages")

    return parse.parse_args()


def read_ini(ini_filename):
    '''
    Open and parse ini file

    Parameters:
        ini_filename (str): name of inifile

    Returns:
        config :(dict): Dictionary of BloxOne configuration elements

    '''
    # Local Variables
    cfg = configparser.ConfigParser()
    config = {}
    ini_keys = ['gm', 'api_version', 'valid_cert', 'user', 'pass']

    # Attempt to read api_key from ini file
    try:
        cfg.read(ini_filename)
    except configparser.Error as err:
        logging.error(err)

    # Look for NIOS section
    if 'NIOS' in cfg:
        for key in ini_keys:
            # Check for key in BloxOne section
            if key in cfg['NIOS']:
                config[key] = cfg['NIOS'][key].strip("'\"")
                logging.debug('Key {} found in {}: {}'.format(key, ini_filename, config[key]))
            else:
                logging.warning('Key {} not found in NIOS section.'.format(key))
                config[key] = ''
    else:
        logging.warning('No BloxOne Section in config file: {}'.format(ini_filename))
        config['api_key'] = ''

    return config

def sanitize_filename(pathname):
    """Return sanitized filename without path information."""

    # Get the base filename without the directory path, convert dashes
    # to underscores, and get rid of other special characters.
    filename = ''
    for c in os.path.basename(pathname):
        if c == '-':
            c = '_'
        if c.isalnum() or c == '_' or c == '.':
            filename += c
    return filename


def upload_csv(config, file, view="default"):
    '''
    Upload CSV and execute
    '''
    status = False
    url = 'https://' + config['gm'] + '/wapi/' + config['api_version'] + '/'
    id = config['user']
    pw = config['pass']
    if config['valid_cert'] == 'true':
        valid_cert = True
    else:
        valid_cert = False

    # Avoid error due to a self-signed cert.
    if not valid_cert:
        requests.packages.urllib3.disable_warnings()

    # The CSV file we want to import (in the local filesystem).
    csv_data = file

    # Initiate a file upload operation, providing a filename (with
    # alphanumeric, underscore, or periods only) for the CSV job manager.
    req_params = {'filename': sanitize_filename(csv_data)}
    r = requests.post(url + 'fileop?_function=uploadinit',
                    auth=(id, pw),
                    verify=valid_cert )
    if r.status_code != requests.codes.ok:
        print(r.text)
        exit_msg = 'Error {} initiating upload: {}'
        sys.exit(exit_msg.format(r.status_code, r.reason))
    results = r.json()

    # Save the authentication cookie for use in subsequent requests.
    ibapauth_cookie = r.cookies['ibapauth']

    # Save the returned URL and token for subsequent requests.
    upload_url = results['url']
    upload_token = results['token']

    # Upload the data in the CSV file.

    # Specify a file handle for the file data to be uploaded.
    req_files = {'filedata': open(csv_data,'rb')}

    # Specify the name of the file (not used?).
    req_params = {'name': sanitize_filename(csv_data)}

    # Use the ibapauth cookie to authenticate instead of userid/password.
    req_cookies = {'ibapauth': ibapauth_cookie}

    # Perform the actual upload. (NOTE: It does NOT return JSON results.)
    r = requests.post(upload_url,
                    params=req_params,
                    files=req_files,
                    cookies=req_cookies,
                    verify=valid_cert)
    if r.status_code != requests.codes.ok:
        sys.exit(exit_msg.format(r.status_code, r.reason))

    # Initiate the actual import task.
    req_params = {'token': upload_token,
                'merge_data': True,
                'network_view': view }
    r = requests.post(url + 'fileop?_function=setdiscoverycsv',
                    params=req_params,
                    cookies=req_cookies,
                    verify=valid_cert)
    if r.status_code in requests.codes.ok:
        status = True
        print('Discovery data imported')
    else:
        status = False
        print(r.text)
        exit_msg = 'Error {} starting discovery import: {}'
        sys.exit(exit_msg.format(r.status_code, r.reason))

    # results = r.json()

    return status


def main():
    '''
    Code logic
    '''
    exitcode = 0

    # Parse CLI arguments
    args = parseargs()
    inifile = args.config
    file = args.file

    # Read inifile
    config = read_ini(inifile)

    upload_csv(config, file, view=args.view)

    return exitcode


### Main ###
if __name__ == '__main__':
    exitcode = main()
    exit(exitcode)
## End Main ###