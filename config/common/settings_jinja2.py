from jinja2 import Undefined, DebugUndefined, StrictUndefined

JINJA2_ENVIRONMENT_OPTIONS = {
    'autoescape': True,
    'undefined': Undefined,
    'auto_reload': True,
    'cache_size': 1000,
}