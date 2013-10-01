#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

if __name__ != '__main__':
    raise Exception('manage.py should be run directly and not be imported')

print "running manage.py ..."

env = os.environ.get('APP_ENV', 'local')
print "app environment:%s" % env

settings_module = 'config.%s.settings' % env
print "settings:%s" % settings_module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

print "executing from command line:%s" % sys.argv
execute_from_command_line(sys.argv)
