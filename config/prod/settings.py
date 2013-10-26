import os
import pymysql
from config.common.settings import *
from boto.s3.connection import OrdinaryCallingFormat

ENV = 'prod'
DEBUG = TEMPLATE_DEBUG = ASSETS_DEBUG = False

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQL_DATABASE'],
        'USER': os.environ['MYSQL_USER'],
        'OPTIONS': {
            'connect_timeout': 10,
            # Disable nagle's algorithm. Assumes your networking to DB is FAST.
            'no_delay': True
        }
    }
}

if 'MYSQL_HOST' in os.environ:
    DATABASES['default']['HOST'] = os.environ['MYSQL_HOST']

if 'MYSQL_PASSWORD' in os.environ:
    DATABASES['default']['PASSWORD'] = os.environ['MYSQL_PASSWORD']

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Jinja2 Optimization
JINJA2_ENVIRONMENT_OPTIONS['auto_reload'] = False

# Static Files to S3
INSTALLED_APPS += ('storages',)

STATICFILES_STORAGE = 'app.core.s3.StaticRootS3BotoStorage'

AWS_STORAGE_BUCKET_NAME = '%s-%s/%s' % (APP_NAME, ENV, RELEASE_NUM)
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_QUERYSTRING_AUTH = False
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

S3_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL