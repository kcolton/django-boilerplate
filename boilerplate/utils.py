import imp
import sys
import os
import re

from boilerplate import logger


def dotenv_load(dotenv_file):
    """
    Loads a given .env file and merges it's contents with os.environ
    """
    try:
        dotenv = imp.load_source('dotenv', dotenv_file)
        dotenv = {attr: getattr(dotenv, attr) for attr in dir(dotenv) if not attr.startswith('_')}
        os.environ.update(dotenv)

        logger.debug('Loading .env vars from: %s' % dotenv_file)
    except IOError:
        pass


def load_environment():
    configuration_arg_check = re.compile('^--configuration=(.+)$')
    configuration_args = filter(configuration_arg_check.match, sys.argv)

    if configuration_args:
        configuration = configuration_arg_check.match(configuration_args[0]).group(1)
        logger.debug('Configuration from arg: %s' % configuration)
        os.environ.setdefault('DJANGO_CONFIGURATION', configuration)
    else:
        logger.debug('Configuration from os.environ')
        os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

    dotenv_load('envs/%s.env' % os.environ['DJANGO_CONFIGURATION'])
