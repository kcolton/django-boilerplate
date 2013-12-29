import imp
import sys
import os
import re
from pprint import pprint


def dotenv_load(dotenv_file):
    """
    Loads a given .env file and merges it's contents with os.environ
    """
    try:
        dotenv = imp.load_source('dotenv', dotenv_file)
        dotenv = {attr: getattr(dotenv, attr) for attr in dir(dotenv) if not attr.startswith('_')}
        os.environ.update(dotenv)

        print "Loading .env vars from: %s" % dotenv_file
        pprint(dotenv)
    except IOError:
        print "%s file not found. skipping." % dotenv_file


def load_environment():
    configuration_arg_check = re.compile('^--configuration=(.+)$')
    configuration_args = filter(configuration_arg_check.match, sys.argv)

    if configuration_args:
        configuration = configuration_arg_check.match(configuration_args[0]).group(1)
        print "Configuration from arg: %s" % configuration
        os.environ.setdefault('DJANGO_CONFIGURATION', configuration)
    else:
        print "Configuration from os.environ"
        os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

    dotenv_load('envs/%s.env' % os.environ['DJANGO_CONFIGURATION'])
