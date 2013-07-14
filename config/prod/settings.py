from config.common.settings import *

ENV = 'prod'

DEBUG = TEMPLATE_DEBUG = False

INSTALLED_APPS += ('storages',)

AWS_STORAGE_BUCKET_NAME = 'djbp'
STATICFILES_STORAGE = 'app.core.s3.StaticRootS3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL

AWS_ACCESS_KEY_ID = 'AKIAIMRPSXJ2CE4ZQEXA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_QUERYSTRING_AUTH = False # Important, otherwise you get a bunch of junk in the generated URLs

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': 'localhost:11211',
#         'KEY_PREFIX': ''
#     }
# }

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'