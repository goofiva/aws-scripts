#!/usr/bin/env python

import os
import sys

from termcolor import colored, cprint

import argparse
import json
script_path, script_name = os.path.split((os.path.dirname(os.path.realpath(__file__))))
sys.path.append(script_path)
import aws_scripts


parser = argparse.ArgumentParser(description='Modify Instance User Data')
parser.add_argument('-t', '--tags', required=True, help="tags in json format. '{\"Name\":\"an-instance-name\"}'")
parser.add_argument('-f', '--file-path', required=True, help='user data file path')
args = parser.parse_args()


tags = args.tags
try:
    tags = json.loads(tags)
except Exception as err:
    cprint('Invalid JSON tags Syntax!', 'red')
    sys.exit(1)

file_path = os.path.abspath(args.file_path)
if not os.path.isfile(file_path):
    cprint('Invalid user-data-file path', 'red')
    sys.exit(1)


print('')
aws_scripts.ec2.modify_instance_user_data(tags=tags, file_path=file_path, dry_run=True)

print('')
print('')
cprint('WARNING: Applying changes will STOP instances!', 'red')
print('')
text = colored("To proceed with applying changes type 'yes' or 'no': ", 'magenta')
apply = input(text)

if apply == "yes":
    aws_scripts.ec2.modify_instance_user_data(tags=tags, file_path=file_path, dry_run=False)
    cprint('Done!', 'green')
else:
    print('Goodbye!')
