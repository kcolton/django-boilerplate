from django.conf import global_settings
from jinja2 import Undefined, DebugUndefined, StrictUndefined

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Add our custom context processors to the default list
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django_boilerplate.context_processor',
    'django_hijax.context_processor',
)

# Jinja2 Optimizations
JINJA2_ENVIRONMENT_OPTIONS = {
    'autoescape': True,
    'undefined': Undefined,
    'auto_reload': True,
    'cache_size': 1000,
}