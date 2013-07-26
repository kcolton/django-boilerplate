from config.common.settings import *

ENV = 'stage'
DEBUG = TEMPLATE_DEBUG = False
WSGI_APPLICATION = 'config.stage.wsgi.application'

# Uncomment the next line if you wish to use AWS S3 + django-storages + Boto for statics
# from settings_s3 import *

ADMINS = (
    ('Errors', 'ken@twubs.com'),
)

# SMTP STTINGS
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'app16994495@heroku.com'
EMAIL_HOST_PASSWORD = 'FlmoE9aZFA56gxwBs0rVSA'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'ken@twubs.com'

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': 'localhost:11211',
#         'KEY_PREFIX': ''
#     }
# }

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'