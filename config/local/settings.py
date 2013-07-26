from config.common.settings import *

ENV = 'local'
ASSETS_DEBUG = True
WSGI_APPLICATION = 'config.local.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(TOP_ROOT, 'db.sqlite'),                 # Or path to database file if using sqlite3.
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

