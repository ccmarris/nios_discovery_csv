#!/usr/bin/perl
############################################################################
# ABSOLUTELY NO WARRANTY WITH THIS PACKAGE. USE IT AT YOUR OWN RISK.
#
# <Description>
#
# Requirements:
#   Perl 5.x      http://www.perl.org
#
# Usage: <scriptname> [options]
#        -d        dump mode (dump message as-is)
#        -t        test mode (no actions taken)
#        -h        help
#        -v        verbose
#
# Author: Chris Marrison
#
# ChangeLog:
#   <date>	<version>	<comment>
#
# Todo:
#
# Copyright (c) 2014 All Rights Reserved.
############################################################################
use strict;
use warnings;
use Infoblox;

### Variables ###
my $Version = 'v0.10';
my $ScriptName = 'sample-import-discovery-csv.pl';
#my $ScriptUrl = "http://spitfire.marrison.net/infoblox/"
my $Copyright = "Copyright (c) 2015 Infoblox Inc. All Rights Reserved.";
#
my $DumpMode = 0; 
my $TestMode = 0; 
my $Verbose = 0;

############
### MAIN ###
############

my $session = Infoblox::Session->new(
	master   => '172.16.137.10',
        username => 'admin',
        password => 'infoblox',

);

if ($session->status_code()) {
    print "Failed to create session: "
          . $session->status_code() . ":" . $session->status_detail();
    exit;
}

#Get a Grid through the session
my $grid = $session->import_data(
	type   => "discovery_csv",
	network_view   => "default",
	path   => "./test-discovery-input.csv" );
unless ( $grid ) {
	die("Get Grid failed: ",
		$session->status_code() . ":" . $session->status_detail());
}
print $grid;


exit 0;

### End MAIN ###

#############################
# Subroutines and Functions #
#############################

