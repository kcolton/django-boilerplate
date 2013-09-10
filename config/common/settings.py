import django.conf.global_settings as DEFAULT_SETTINGS
import os

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

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


INSTALLED_APPS = (
    'app',
    'app.core',

    'coffin',
    'django_assets',
    'widget_tweaks',
    'djorm_pool',
    # 'debug_toolbar',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    # Uncomment the next line if we are using db backed sessions. Otherwise only the middleware is needed
    'django.contrib.sessions',

    'django.contrib.messages',
    'django.contrib.staticfiles',

    'suit',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

# Add our custom context processors to the default list
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'app.core.context_processors.request',
)

AUTH_USER_MODEL = 'app.User'

# Additional specific settings
from settings_jinja2 import *
from settings_logging import *