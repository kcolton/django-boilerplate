from config.common.settings import *

ENV = 'prod'
DEBUG = TEMPLATE_DEBUG = False
WSGI_APPLICATION = 'config.prod.wsgi.application'

# Uncomment the next line if you wish to use AWS S3 + django-storages + Boto for statics
# from settings_s3 import *

ADMINS = (
    ('Errors', 'ken@twubs.com'),
)

# SMTP STTINGS
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'app16981690@heroku.com'
EMAIL_HOST_PASSWORD = 'zz7UMm865O77mis14zgSFw'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'ken@twubs.com'

JINJA2_ENVIRONMENT_OPTIONS['auto_reload'] = False

# CACHES = {
#     'default': {
#         'BACKEND': 'lib.django.cache.memcached.ConsistentMemcachedCache',
#         'LOCATION': 'localhost:11211',
#         'KEY_PREFIX': ''
#     }
# }

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

