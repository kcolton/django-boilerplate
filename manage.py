#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line
from django_boilerplate.utils import safety_check, dotenv_load

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
os.environ['APP_CONFIG'] = APP_CONFIG


# Merge in .env files to os.environ
dotenv_load('config/common/.env')
dotenv_load('config/%s/.env' % APP_CONFIG)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

safety_check()

print "Executing from command line:%s" % sys.argv
execute_from_command_line(sys.argv)
