# Copy-paste. Do not import directly

from boto.s3.connection import OrdinaryCallingFormat

INSTALLED_APPS += ('storages',)

# Default bucket name that uses APP_NAME-ENV/RELEASE_NUM format which works well in many situations
# Optional: Add the RELEASE_NUM to the bucket for cache busting
AWS_STORAGE_BUCKET_NAME = '%s-%s/%s' % (APP_NAME, ENV, RELEASE_NUM)

STATICFILES_STORAGE = 'app.core.s3.StaticRootS3BotoStorage'

# Don't commit these or you may be a sad panda
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

# Important! otherwise you get a bunch of junk in the generated URLs
AWS_QUERYSTRING_AUTH = False

# Important! Otherwise you get SSL warnings and embedded assets don't load
# OrdinaryCallingFormat = s3.amazonaws.com/bucket instead of bucket.s3.amazonaws.com
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

S3_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL