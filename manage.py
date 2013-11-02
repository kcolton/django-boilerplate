#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line
from lib import utils
from lib.django.utils.sanity import check_sanity

if __name__ != '__main__':
    raise Exception("manage.py should be run directly and not be imported")

try:
    config_pos = sys.argv.index('--app-config')
    APP_CONFIG = sys.argv.pop(config_pos + 1)
    sys.argv.pop(config_pos)
except IndexError:
    raise Exception("You must supply a configuration with --app-config")
except ValueError:
    APP_CONFIG = os.environ.get('APP_CONFIG', 'local')

print "MANAGE APP_CONFIG:%s" % APP_CONFIG

settings_module = 'config.%s.settings' % APP_CONFIG
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

# Merge in .env files to os.environ.
utils.dotenv_load('config/common/.env')
utils.dotenv_load('config/%s/.env' % APP_CONFIG)

# Look for red flags
check_sanity()

print "Executing from command line:%s" % sys.argv
execute_from_command_line(sys.argv)
