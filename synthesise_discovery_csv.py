#!/usr/bin/env python3
#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
'''

 Description:

    Generate Discovery Metadata CSV File

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
__version__ = '0.0.1'
__author__ = 'Chris Marrison'
__author_email__ = 'chris@infoblox.com'

import logging
import argparse
import json
import ipaddress
import os
import sys
import requests
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
    parse.add_argument('-m', '--monitor', action='store_true', 
                        help="Monitor Status of Import")
    parse.add_argument('-s', '--status', type=str, 
                        help="Get Status of CSV Import Job Specified")
    parse.add_argument('-a', '--action', type=str, 
                        help="Change default action of INSERT (e.g. DELETE) for CSV Import")
    parse.add_argument('-d', '--debug', action='store_true', 
                        help="Enable debug messages")

    return parse.parse_args()


def import_fields(filename:str = 'discovery_fields.json'):
	'''
    '''
	try:
		logging.info(f'Loading field definitions from: {filename}')
		f = open(filename)
		fields = json.load(f)
		logging.info('Field definitions loaded')
	except:
		logging.error(f'Failed to import field definitions from: {filename}')
		raise

	return fields


def build_field_test(filename:str = 'field_test_import.csv',
                      fields:dict = {}):
    '''
    '''
    field_names: list
    ipv4: ipaddress.IPv4Address 
    octet: int

    logging.info('Generating field list')
    for field in fields.keys():
        field_names.append(fields.get(field))
    
    logging.info('')

    for index in range(len(field_names)):
        octet = 10 + index
        ipv4 = ipaddress.ip_address(f'192.168.1.{octet}')
        
        
        
        


	
	

	


def main():
    '''
    Code logic
    '''
    exitcode = 0

    # Parse CLI arguments
    args = parseargs()
    file = args.file

    return exitcode


### Main ###
if __name__ == '__main__':
    exitcode = main()
    exit(exitcode)
## End Main ###