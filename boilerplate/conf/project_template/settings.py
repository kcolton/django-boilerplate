import os
import logging

import pymysql
from configurations import values
from boilerplate.conf import configs

pymysql.install_as_MySQLdb()

ENV_LOCAL = 'local'
ENV_DEV = 'dev'
ENV_STAGE = 'stage'
ENV_PROD = 'prod'

STORAGE_LOCAL = 'local'
STORAGE_DEV = 'dev'
STORAGE_PROD = 'prod'


class AppBase(configs.Base):
    APP_NAME = '{{ project_name }}'
    RELEASE_NUM = 1

    TITLE = '{{ project_name }}'

    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

    WSGI_APPLICATION = 'wsgi.application'
    ROOT_URLCONF = 'urls'
    AUTH_USER_MODEL = '{{ project_name }}.User'

    TIME_ZONE = 'America/New_York'
    LANGUAGE_CODE = 'en-us'

    INSTALLED_APPS = (
        '{{ project_name }}',

        'hijax',
        'boilerplate',

        'coffin',
        'widget_tweaks',
        'pipeline',

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

        'hijax.plugins.Middleware',

        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collectedstatic')
    MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
    DATABASES = values.DatabaseURLValue('sqlite:///' + os.path.join(PROJECT_ROOT, 'data/db.sqlite'))

    SESSION_ENGINE = 'django.contrib.sessions.backends.db'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s: %(name)s %(levelname)s - %(message)s'
            }
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'debug_console': {
                'class': 'logging.StreamHandler',
                'filters': ['require_debug_true'],
                'formatter': 'simple'
            },
            'console': {
                'class': 'logging.StreamHandler',
                'filters': ['require_debug_false'],
                'level': logging.WARNING,
                'formatter': 'simple'
            },
            'null': {
                'class': 'django.utils.log.NullHandler',
            }
        },
        'loggers': {
            'django': {
                'level': logging.NOTSET,
                'handlers': [],
                'propagate': True
            },
            'django.request': {
                'level': logging.NOTSET,
                'handlers': [],
                'propagate': True
            },
            'py.warnings': {
                'level': logging.NOTSET,
                'handlers': [],
                'propagate': True
            },
        },
        'root': {
            'level': logging.NOTSET,
            'handlers': ['debug_console', 'console']
        }
    }


class Local(AppBase):
    ENV = ENV_LOCAL
    STORAGE = STORAGE_LOCAL

    DEBUG = TEMPLATE_DEBUG = True


class LocalCompress(configs.CompressAssets, Local):
    pass


class LocalNoDebug(Local):
    DEBUG = TEMPLATE_DEBUG = False


class Dev(configs.S3Assets, configs.CompressAssets, AppBase):
    ENV = ENV_DEV
    STORAGE = STORAGE_DEV

    DEBUG = TEMPLATE_DEBUG = True


class Prod(configs.S3Assets, configs.CompressAssets, AppBase):
    ENV = ENV_PROD
    STORAGE = STORAGE_PROD

    DEBUG = TEMPLATE_DEBUG = False
    # add jinja2 options


class Stage(Prod):
    ENV = ENV_STAGE
