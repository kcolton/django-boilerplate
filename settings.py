import os

from configurations import Configuration, values
from django_boilerplate.config import defaults


ENV_LOCAL = 'local'
ENV_DEV = 'dev'
ENV_STAGE = 'stage'
ENV_PROD = 'prod'

STORAGE_LOCAL = 'local'
STORAGE_DEV = 'dev'
STORAGE_PROD = 'prod'


class Base(Configuration):
    ENV = ENV_LOCAL
    APP_NAME = 'djbp'
    RELEASE_NUM = 1

    TITLE = 'DJBP'

    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    APP_ROOT = os.path.join(PROJECT_ROOT, 'app')

    TEMPLATE_DEBUG = DEBUG = ASSETS_DEBUG = True

    WSGI_APPLICATION = 'wsgi.application'
    ROOT_URLCONF = 'app.urls'
    AUTH_USER_MODEL = 'django_boilerplate.User'

    MANAGERS = ADMINS = ()

    INSTALLED_APPS = (
        'django_hijax',
        'django_boilerplate',
        'app',

        'coffin',
        'django_assets',
        'widget_tweaks',

        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'suit',
        'django.contrib.admin',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',

        'django_hijax.Middleware',

        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

    TEMPLATE_CONTEXT_PROCESSORS = defaults.CONTEXT_PROCESSORS
    TEMPLATE_LOADERS = defaults.TEMPLATE_LOADERS
    STATICFILES_FINDERS = defaults.STATICFILES_FINDERS
    LOGGING = defaults.LOGGING
    JINJA2_ENVIRONMENT_OPTIONS = defaults.JINJA2_ENVIRONMENT_OPTIONS_DEV

    # Localization

    TIME_ZONE = 'America/New_York'
    LANGUAGE_CODE = 'en-us'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Security

    # Override in environment specific settings or .env file
    DEFAULT_SECRET_KEY = 'unsecure_default_secret'
    SECRET_KEY = values.Value(default=DEFAULT_SECRET_KEY)

    ALLOWED_HOSTS = ['*']

    # Assets & Statics

    # Build into app static folder so both local and collect static works
    ASSETS_ROOT = os.path.join(APP_ROOT, 'static')
    ASSETS_AUTO_BUILD = False
    ASSETS_URL_EXPIRE = False
    ASSETS_CACHE = False
    ASSETS_MANIFEST = False

    STATIC_ROOT = os.path.join(APP_ROOT, 'collectedstatic')
    STATIC_URL = '/static/'

    MEDIA_ROOT = os.path.join(APP_ROOT, 'media')
    MEDIA_URL = '/media/'


class Local(Base):
    ENV = ENV_LOCAL
    STORAGE = STORAGE_LOCAL

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(Base.PROJECT_ROOT, 'data/db.sqlite'),
        }
    }

    SESSION_ENGINE = 'django.contrib.sessions.backends.file'


class Dev(Base):
    ENV = ENV_DEV
    STORAGE = STORAGE_DEV


class Prod(Base):
    import os
    import pymysql

    from boto.s3.connection import OrdinaryCallingFormat

    pymysql.install_as_MySQLdb()

    ENV = ENV_PROD
    STORAGE = STORAGE_PROD

    DEBUG = TEMPLATE_DEBUG = ASSETS_DEBUG = False

    MYSQL_DATABASE = values.Value()
    MYSQL_USER = values.Value()
    MYSQL_HOST = values.Value()
    MYSQL_PASSWORD = values.Value()

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': MYSQL_DATABASE,
            'USER': MYSQL_USER,
            'OPTIONS': {
                'connect_timeout': 5,
                # Disable nagle's algorithm. Assumes your networking to DB is FAST.
                'no_delay': True
            }
        }
    }


    if MYSQL_HOST:
        DATABASES['default']['HOST'] = MYSQL_HOST

    if MYSQL_PASSWORD:
        DATABASES['default']['PASSWORD'] = MYSQL_PASSWORD

    SESSION_ENGINE = 'django.contrib.sessions.backends.db'

    INSTALLED_APPS = Base.INSTALLED_APPS + ('storages',)

    STATICFILES_STORAGE = 'django_boilerplate.storage.ReleaseStaticsS3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_STORAGE_BUCKET_NAME = '%s-%s' % (Base.APP_NAME, STORAGE)
    AWS_ACCESS_KEY_ID = values.Value()
    AWS_SECRET_ACCESS_KEY = values.Value()
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

    STATIC_PREFIX = 'static/%d/' % Base.RELEASE_NUM
    S3_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL + STATIC_PREFIX

    JINJA2_ENVIRONMENT_OPTIONS = defaults.JINJA2_ENVIRONMENT_OPTIONS_RELEASE


class Stage(Prod):
    ENV = ENV_STAGE