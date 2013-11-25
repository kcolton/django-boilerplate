from django.utils.timezone import utc, localtime, make_naive, get_current_timezone
from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


class ReleaseStaticsS3BotoStorage(S3BotoStorage):

    def __init__(self, *args, **kwargs):
        super(ReleaseStaticsS3BotoStorage, self).__init__(*args, location=settings.STATIC_PREFIX, **kwargs)

    def modified_time(self, name):
        """
            HACK HACK HACK. For whatever reason S3 timezone doesn't get converted back
            to local time here, so we have to change the mod_time or else `collectstatic`
            won't update any files to the server.
        """
        mod_time = super(ReleaseStaticsS3BotoStorage, self).modified_time(name)

        mod_time = mod_time.replace(tzinfo=utc) # Make timezone aware
        mod_time = localtime(mod_time) # Convert to local timezone
        mod_time = make_naive(mod_time, get_current_timezone()) # Make naive again
        return mod_time