#!/usr/bin/env python
import os
import sys
import imp

import django.core.management

import boilerplate.utils
from boilerplate import logger


if __name__ != '__main__':
    raise Exception("manage.py should be run directly and not be imported")


# Load environment from configuration
boilerplate.utils.load_environment()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

try:
    # ugly - disgusting - crap
    imp.find_module(os.environ['DJANGO_SETTINGS_MODULE'])

    import configurations.management

    logger.debug('Executing from command line: %s' % sys.argv)
    configurations.management.execute_from_command_line(sys.argv)

except ImportError:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'boilerplate.conf.empty_settings'
    django.core.management.execute_from_command_line(sys.argv)


