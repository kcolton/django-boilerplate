import logging
import sys


# Note: If you are using foreman. Make sure to have PYTHONUNBUFFERED="True" in your .env file
# Otherwise, you will not see stdout or stderr output

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