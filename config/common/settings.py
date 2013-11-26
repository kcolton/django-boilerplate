import os

from django_boilerplate.config import defaults

from . import environments

ENV = environments.ENV_LOCAL
APP_NAME = 'djbp'
RELEASE_NUM = 1

TITLE = 'DJBP'

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
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
SECRET_KEY = os.environ.get('SECRET_KEY', DEFAULT_SECRET_KEY)

ALLOWED_HOSTS = ['*']

# Assets & Statics

ASSETS_ROOT = os.path.join(APP_ROOT, 'static')  # Build into app static folder so both local and collect static works
ASSETS_AUTO_BUILD = False
ASSETS_URL_EXPIRE = False
ASSETS_CACHE = False
ASSETS_MANIFEST = False

STATIC_ROOT = os.path.join(APP_ROOT, 'collectedstatic')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(APP_ROOT, 'media')
MEDIA_URL = '/media/'
