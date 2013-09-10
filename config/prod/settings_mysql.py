import os
import pymysql
pymysql.install_as_MySQLdb()

if not 'MYSQL_DATABASE' in os.environ:
    raise Exception('Expecting MYSQL_DATABASE environment variable to exist')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',   # Or path to database file if using sqlite3.
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', None),
        'HOST': os.environ.get('MYSQL_HOST', None)
    }
}

DJORM_POOL_OPTIONS = {
    "pool_size": 5,
    "max_overflow": 0,
    "recycle": 3600, # the default value
}