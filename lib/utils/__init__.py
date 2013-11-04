import imp
import os
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