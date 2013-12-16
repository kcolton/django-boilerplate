
import os

from boto.s3.connection import OrdinaryCallingFormat
from configurations import Configuration, values
from jinja2 import Undefined, DebugUndefined, StrictUndefined
from django_boilerplate import assets

import inspect
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
    APP_ROOT = None

    WSGI_APPLICATION = None
    ROOT_URLCONF = None
    AUTH_USER_MODEL = None

    GOOGLE_TAG_MANAGER_CONTAINER = values.Value(None, environ_prefix=None)

    MANAGERS = ADMINS = ()

    INSTALLED_APPS = (
        'django_hijax',
        'django_boilerplate',

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

        'django_hijax.Middleware',

        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

    TEMPLATE_CONTEXT_PROCESSORS = Configuration.TEMPLATE_CONTEXT_PROCESSORS + (
        'django_boilerplate.context_processors.context_processor',
        'django_hijax.context_processor',
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
    DEFAULT_SECRET_KEY = 'unsecure_default_secret'
    SECRET_KEY = values.Value(default=DEFAULT_SECRET_KEY, environ_prefix=None)

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

    JINJA2_EXTENSIONS = [
        'pipeline.jinja2.ext.PipelineExtension'
    ]

    SESSION_ENGINE = 'django.contrib.sessions.backends.db'

    @classmethod
    def pre_setup(cls):
        super(Base, cls).pre_setup()
        cls.pre_setup_mixins()

    @classmethod
    def pre_setup_mixins(cls):
        for base in inspect.getmro(cls):
            if not issubclass(base, Configuration) and hasattr(base, 'pre_setup_mixin'):
                base.pre_setup_mixin(cls)

    @classmethod
    def setup(cls):
        cls.STATIC_ROOT = os.path.join(cls.APP_ROOT, 'collectedstatic')
        cls.MEDIA_ROOT = os.path.join(cls.APP_ROOT, 'media')

        cls.DATABASES = values.DatabaseURLValue('sqlite:///' + os.path.join(cls.PROJECT_ROOT, 'data/db.sqlite'))

        super(Base, cls).setup()
        cls.setup_mixins()

    @classmethod
    def setup_mixins(cls):
        for base in inspect.getmro(cls):
            if not issubclass(base, Configuration) and hasattr(base, 'setup_mixin'):
                base.setup_mixin(cls)

    @classmethod
    def post_setup(cls):
        from django.conf import settings
        js_assets, css_assets = assets.autodiscover_assets(settings.INSTALLED_APPS)

        settings.PIPELINE_JS['main']['source_filenames'] += js_assets
        settings.PIPELINE_CSS['main']['source_filenames'] += css_assets

        super(Base, cls).post_setup()
        cls.post_setup_mixins()

    @classmethod
    def post_setup_mixins(cls):
        for base in inspect.getmro(cls):
            if not issubclass(base, Configuration) and hasattr(base, 'post_setup_mixin'):
                base.post_setup_mixin(cls)


class CompressAssets(object):
    PIPELINE_ENABLED = True
    PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
    PIPELINE_CSS_COMPRESSOR = None
    PIPELINE_COMPILERS = ('pipeline.compilers.less.LessCompiler',)
    STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

    @classmethod
    def pre_setup(cls):
        cls.pre_setup_mixin(cls)
        super(CompressAssets, cls).pre_setup()

    @staticmethod
    def pre_setup_mixin(cls):
        cls.STATICFILES_FINDERS += ('pipeline.finders.PipelineFinder', )


class S3Assets(object):
    AWS_ACCESS_KEY_ID = values.SecretValue(environ_prefix=None)
    AWS_SECRET_ACCESS_KEY = values.SecretValue(environ_prefix=None)
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
    AWS_IS_GZIPPED = True

    STATICFILES_STORAGE = 'django_boilerplate.storage.ReleaseStaticsS3BotoStorage'

    @classmethod
    def setup(cls):
        cls.setup_mixin(cls)
        super(S3Assets, cls).setup()

    @staticmethod
    def setup_mixin(cls):
        cls.INSTALLED_APPS += ('storages',)
        cls.AWS_STORAGE_BUCKET_NAME = '%s-%s' % (cls.APP_NAME, cls.STORAGE)
        cls.STATIC_PREFIX = 'static/%s/%d/' % (cls.ENV, cls.RELEASE_NUM)
        cls.S3_URL = 'http://s3.amazonaws.com/%s/' % cls.AWS_STORAGE_BUCKET_NAME
        cls.STATIC_URL = cls.S3_URL + cls.STATIC_PREFIX
