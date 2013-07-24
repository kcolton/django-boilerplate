from config.common.settings import *
from boto.s3.connection import OrdinaryCallingFormat

ENV = 'prod'

DEBUG = TEMPLATE_DEBUG = False

INSTALLED_APPS += ('storages',)

AWS_STORAGE_BUCKET_NAME = 'djbp-prod/%s' % RELEASE_NUM
STATICFILES_STORAGE = 'app.core.s3.StaticRootS3BotoStorage'
S3_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL

AWS_ACCESS_KEY_ID = 'AKIAIMRPSXJ2CE4ZQEXA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_QUERYSTRING_AUTH = False # Important! otherwise you get a bunch of junk in the generated URLs
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat() # Important! Otherwise you get SSL warnings and embedded things don't load

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
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': 'localhost:11211',
#         'KEY_PREFIX': ''
#     }
# }

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'