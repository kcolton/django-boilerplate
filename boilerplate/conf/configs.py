import os

from boto.s3.connection import OrdinaryCallingFormat
from configurations import Configuration, values
from jinja2 import Undefined, DebugUndefined, StrictUndefined
from boilerplate import assets

import logging

ENV_LOCAL = 'local'
ENV_DEV = 'dev'
ENV_STAGE = 'stage'
ENV_PROD = 'prod'

STORAGE_LOCAL = 'local'
STORAGE_DEV = 'dev'
STORAGE_PROD = 'prod'


class Base(Configuration):
    ENV = ENV_LOCAL
    TEMPLATE_DEBUG = DEBUG = True

    # Overwrite in app settings
    RELEASE_NUM = 1
    APP_NAME = 'djbp'
    TITLE = 'DJBP'

    PROJECT_ROOT = None

    WSGI_APPLICATION = None
    ROOT_URLCONF = None
    AUTH_USER_MODEL = None

    GOOGLE_TAG_MANAGER_CONTAINER = values.Value(None, environ_prefix=None)

    MANAGERS = ADMINS = ()

    INSTALLED_APPS = (
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

    TEMPLATE_CONTEXT_PROCESSORS = Configuration.TEMPLATE_CONTEXT_PROCESSORS + (
        'boilerplate.context_processors.context_processor',
        'hijax.plugins.context_processor',
    )

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    JINJA2_ENVIRONMENT_OPTIONS = {
        'autoescape': True,
        'undefined': Undefined,
        'auto_reload': True,
        'cache_size': 1000,
    }

    # Logging

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
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

    # Localization

    TIME_ZONE = 'America/New_York'
    LANGUAGE_CODE = 'en-us'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Security

    # Override in environment specific settings or .env file
    SECRET_KEY = values.Value(environ_prefix=None)

    ALLOWED_HOSTS = ['*']

    # Statics

    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

    # Assets

    PIPELINE_ENABLED = False

    # actual filenames will be auto-discovered and added in post_setup

    PIPELINE_JS = {
        'main': {
            'source_filenames': [],
            'output_filename': 'dist/main.js',
        },
    }

    PIPELINE_CSS = {
        'main': {
            'source_filenames': [],
            'output_filename': 'dist/main.css',
        },
    }

    SYNCSTATIC_IGNORE_PATTERNS = [
        '*.less',
    ]

    JQUERY_UI = True
    LODASH = True
    CDN_LIBRARIES = True


    JINJA2_EXTENSIONS = [
        'pipeline.jinja2.ext.PipelineExtension'
    ]

    SESSION_ENGINE = 'django.contrib.sessions.backends.db'

    print('Base class namespace')

    @classmethod
    def setup(cls):
        cls.STATIC_ROOT = os.path.join(cls.PROJECT_ROOT, 'collectedstatic')
        cls.MEDIA_ROOT = os.path.join(cls.PROJECT_ROOT, 'media')
        cls.DATABASES = values.DatabaseURLValue('sqlite:///' + os.path.join(cls.PROJECT_ROOT, 'data/db.sqlite'))

        super(Base, cls).setup()


    @classmethod
    def post_setup(cls):
        super(Base, cls).post_setup()

        from django.conf import settings
        app_assets = assets.AppAssets.autodiscover(settings.INSTALLED_APPS)

        settings.PIPELINE_JS['main']['source_filenames'] += app_assets.js_libraries + app_assets.js_app_scripts
        settings.PIPELINE_CSS['main']['source_filenames'] += app_assets.css_libraries + app_assets.css_app_styles


class CompressAssets(object):
    PIPELINE_ENABLED = True
    PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
    PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
    PIPELINE_COMPILERS = ('pipeline.compilers.less.LessCompiler',)

    # Do our compilation on the collected statics
    PIPELINE_STORAGE = 'pipeline.storage.PipelineStorage'
    STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

    @classmethod
    def setup(cls):
        cls.STATICFILES_FINDERS += ('pipeline.finders.PipelineFinder', )
        super(CompressAssets, cls).setup()


class S3Assets(object):
    AWS_ACCESS_KEY_ID = values.SecretValue(environ_prefix=None)
    AWS_SECRET_ACCESS_KEY = values.SecretValue(environ_prefix=None)

    # Use protocol-less // format for auto switching between http and https
    AWS_S3_SECURE_URLS = False
    AWS_S3_URL_PROTOCOL = ''
    AWS_QUERYSTRING_AUTH = False
    # Use / form
    AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

    STATICFILES_STORAGE = 'boilerplate.storage.ReleaseStaticsS3BotoStorage'

    # Cache statics for a year. That's why we have the release number for cache busting :)
    AWS_HEADERS = {
        'Cache-Control': 'public, max-age=31556926'
    }

    # Gzip
    AWS_IS_GZIPPED = True
    GZIP_CONTENT_TYPES = {
        'text/css',
        'application/javascript',
        'application/x-javascript',
        'image/svg+xml'
    }

    @classmethod
    def setup(cls):
        cls.INSTALLED_APPS += ('storages',)

        if not hasattr(cls, 'AWS_STORAGE_BUCKET_NAME'):
            cls.AWS_STORAGE_BUCKET_NAME = '%s-%s' % (cls.APP_NAME, cls.STORAGE)

        if not hasattr(cls, 'STATIC_PREFIX'):
            cls.STATIC_PREFIX = 'static/%s/%d/' % (cls.ENV, cls.RELEASE_NUM)

        if not hasattr(cls, 'S3_URL'):
            cls.S3_URL = '//s3.amazonaws.com/%s/' % cls.AWS_STORAGE_BUCKET_NAME


        if hasattr(cls, 'AWS_S3_CUSTOM_DOMAIN'):
            cls.STATIC_URL = '//' + cls.AWS_S3_CUSTOM_DOMAIN + '/' + cls.STATIC_PREFIX
        else:
            cls.STATIC_URL = cls.S3_URL + cls.STATIC_PREFIX

        super(S3Assets, cls).setup()




