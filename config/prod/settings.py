import os
import pymysql
from config.common.settings import *
from boto.s3.connection import OrdinaryCallingFormat

pymysql.install_as_MySQLdb()

ENV = ENV_PROD
STORAGE = STORAGE_PROD

DEBUG = TEMPLATE_DEBUG = ASSETS_DEBUG = False

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

JINJA2_ENVIRONMENT_OPTIONS['auto_reload'] = False

INSTALLED_APPS += ('storages',)

STATICFILES_STORAGE = 'lib.django.files.storage.ReleaseStaticsS3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_STORAGE_BUCKET_NAME = '%s-%s' % (APP_NAME, STORAGE)
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_QUERYSTRING_AUTH = False
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

STATIC_PREFIX = 'static/%d/' % RELEASE_NUM
S3_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL + STATIC_PREFIX