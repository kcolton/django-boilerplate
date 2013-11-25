import os
from django.core.wsgi import get_wsgi_application
from django_boilerplate.utils import safety_check

APP_CONFIG = os.environ.get('APP_CONFIG', 'local')
print "WSGI APP_CONFIG:%s" % APP_CONFIG

settings_module = 'config.%s.settings' % APP_CONFIG

# Defer to DJANGO_SETTINGS_MODULE env var if it exits
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()

from django.conf import settings, global_settings

safety_check()

if not settings.DEBUG and settings.STATICFILES_STORAGE == global_settings.STATICFILES_STORAGE:
    # If we are using default staticfiles storage and not in DEBUG, serve through Cling WSGI middleware
    print "WSGI USING CLING"
    from dj_static import Cling
    application = Cling(application)