import django.conf.global_settings as DEFAULT_SETTINGS
import os, sys
from jinja2 import Undefined, DebugUndefined, StrictUndefined

import pymysql
pymysql.install_as_MySQLdb()

# Django settings for green project.

ENV = ''
RELEASE_NUM = 1

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) # 2 levels up from here
TOP_ROOT = os.path.dirname(PROJECT_ROOT)
APP_ROOT = os.path.join(TOP_ROOT, 'app')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

INTERNAL_IPS = ('127.0.0.1',)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    },
    'legacy': { } # Connection information for our legacy database
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(APP_ROOT, 'collectedstatic')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Assets Config
ASSETS_ROOT = os.path.join(APP_ROOT, 'static') # Build into app static folder so both local and collect static works
ASSETS_DEBUG = False
ASSETS_AUTO_BUILD = False # Never auto build assets. Use fab file instead
ASSETS_URL_EXPIRE = False
ASSETS_CACHE = False
ASSETS_MANIFEST = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8%i)pbdkgo(^6m+xil_8%qd)$cj8)gm=egq3+7%_*d7xh%=4kv'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',

    'app.core.middleware.CoreMiddleware',

    # 'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    # Uncomment the next line for csrf verification
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Uncomment the next line for flash messaging support. Maybe we will use this 
    'django.contrib.messages.middleware.MessageMiddleware',

    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'config.local.wsgi.application' # Not sure how this is actually used

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


INSTALLED_APPS = (
    'app',

    'app.core',
    'app.api',
    'app.mobile',
    'app.web',

    'coffin',
    'django_assets',
    # 'debug_toolbar',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    # Uncomment the next line if we are using db backed sessions. Otherwise only the middleware is needed
    'django.contrib.sessions',
    # Uncomment the next line 
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'suit',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# Add our custom context processors to the default list
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'app.core.context_processors.request',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'stream': sys.stdout
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

JINJA2_ENVIRONMENT_OPTIONS = {
    'autoescape': True,
    'undefined': Undefined,
    'auto_reload': True,
    'cache_size': 1000,
}

# Base authentication configuration
# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'profile'
# LOGOUT_URL = 'logout'