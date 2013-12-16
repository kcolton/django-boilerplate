#!/usr/bin/env python
import os
import sys
import importlib

import django.core.management

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
    APP_CONFIG = os.environ.get('APP_CONFIG', 'Local')

print "MANAGE APP_CONFIG:%s" % APP_CONFIG
os.environ['DJANGO_CONFIGURATION'] = APP_CONFIG
os.environ['APP_CONFIG'] = APP_CONFIG


# ugly - disgusting - crap

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

try:
    importlib.import_module(os.environ['DJANGO_SETTINGS_MODULE'])

    import configurations.management

    # Merge in .env files to os.environ
    dotenv_load('envs/%s.env' % APP_CONFIG)

    # safety_check()

    print "Executing from command line:%s" % sys.argv
    configurations.management.execute_from_command_line(sys.argv)

except ImportError:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_boilerplate.conf.empty_settings'
    django.core.management.execute_from_command_line(sys.argv)

    from django.conf import settings
    print "INSTALLED: %s" % settings.INSTALLED_APPS


