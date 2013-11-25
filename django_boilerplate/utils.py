import imp
import os
from pprint import pprint

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


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


def safety_check():
    """
    Look for red flags in the Django setup
    """
    if not settings.DEBUG and settings.SECRET_KEY == settings.DEFAULT_SECRET_KEY:
        raise ImproperlyConfigured('Unique SECRET_KEY required when DEBUG=False')

