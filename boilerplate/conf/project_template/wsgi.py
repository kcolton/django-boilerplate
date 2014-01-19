import os

import boilerplate.utils
from boilerplate import logger


boilerplate.utils.load_environment()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.conf import settings, global_settings


if not settings.DEBUG and settings.STATICFILES_STORAGE == global_settings.STATICFILES_STORAGE:
    # If we are using default staticfiles storage and not in DEBUG, serve through Cling WSGI middleware
    logger.debug('WSGI USING CLING')
    from dj_static import Cling
    application = Cling(application)