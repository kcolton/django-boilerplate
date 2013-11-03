import os

ENV = ''
APP_NAME = 'djbp'
RELEASE_NUM = 1

TITLE = 'DJBP'

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
APP_ROOT = os.path.join(PROJECT_ROOT, 'app')

TEMPLATE_DEBUG = DEBUG = ASSETS_DEBUG = True

WSGI_APPLICATION = 'wsgi.application'
ROOT_URLCONF = 'app.urls'
AUTH_USER_MODEL = 'app.User'

MANAGERS = ADMINS = ()

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',

    'app.middleware.AppMiddleware',

    # 'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'app',

    'coffin',
    'django_assets',
    'widget_tweaks',
    # 'djorm_pool',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'suit',
    'django.contrib.admin',
)

# Additional specific settings
from .settings_security import *
from .settings_localization import *
from .settings_templates import *
from .settings_static import *
from .settings_logging import *
