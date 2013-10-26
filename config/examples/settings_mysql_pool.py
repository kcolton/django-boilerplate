# Copy-paste. Do not import directly

import os
import pymysql


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


# See SQL alchemy pool config options
DJORM_POOL_OPTIONS = {
    "pool_size": 5,
    "max_overflow": 0,
    "recycle": 3600,
}

INSTALLED_APPS += ('djorm_pool',)