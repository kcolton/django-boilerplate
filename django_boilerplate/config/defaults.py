import logging
from jinja2 import Undefined, DebugUndefined, StrictUndefined
from django.conf import global_settings

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

CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django_boilerplate.context_processor',
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

JINJA2_ENVIRONMENT_OPTIONS_DEV = {
    'autoescape': True,
    'undefined': Undefined,
    'auto_reload': True,
    'cache_size': 1000,
}

JINJA2_ENVIRONMENT_OPTIONS_RELEASE = {
    'autoescape': True,
    'undefined': Undefined,
    'auto_reload': False,
    'cache_size': 1000,
}
