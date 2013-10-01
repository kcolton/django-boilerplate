#!/usr/bin/env python
import os
import sys
import imp
import pprint
from django.core.management import execute_from_command_line
from lib.django.utils.sanity import check_sanity

if __name__ != '__main__':
    raise Exception('manage.py should be run directly and not be imported')

APP_CONFIG = os.environ.get('APP_CONFIG', 'local')
print "MANAGE APP_CONFIG:%s" % APP_CONFIG

settings_module = 'config.%s.settings' % APP_CONFIG
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

def dotenv_load(dotenv_file):
    """
    Loads a given .env file and merges it's contents with os.environ
    """
    try:
        dotenv = imp.load_source('dotenv', dotenv_file)
        dotenv = {attr:getattr(dotenv, attr) for attr in dir(dotenv) if not attr.startswith('_')}
        os.environ.update(dotenv)

        print "Loading .env vars from: %s" % dotenv_file
        pprint.pprint(dotenv)
    except IOError:
        print "%s file not found. skipping." % dotenv_file

# Merge in .env files to os.environ. We are kind of cheating by having .env files that
# have the same syntax as a python module where every attribute is a string

dotenv_load('config/common/.env')
dotenv_load('config/%s/.env' % APP_CONFIG)

# Look for red flags
check_sanity()

print "Executing from command line:%s" % sys.argv
execute_from_command_line(sys.argv)
