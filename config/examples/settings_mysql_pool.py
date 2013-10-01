# Copy-paste. Do not import directly

import os
import pymysql
pymysql.install_as_MySQLdb()

if not 'MYSQL_DATABASE' in os.environ:
    raise Exception('Expecting MYSQL_DATABASE environment variable to exist')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQL_DATABASE'],
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', None),
        'HOST': os.environ.get('MYSQL_HOST', None),
        'OPTIONS': {
            'connect_timeout': 10,
            # Disable nagle's algorithm. Assumes your networking to DB is FAST.
            'no_delay': True
        }
    }
}

DJORM_POOL_OPTIONS = {
    "pool_size": 5,
    "max_overflow": 0,
    "recycle": 3600, # the default value
}

INSTALLED_APPS += ('djorm_pool',)