import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                             # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                             # Set to empty string for default.
    }
}

DJORM_POOL_OPTIONS = {
    "pool_size": 5,
    "max_overflow": 0,
    "recycle": 3600, # the default value
}