import os

from django.contrib.staticfiles import utils
from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.core.management import BaseCommand

from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        local_storage = StaticFilesStorage()
        base_path = local_storage.base_location

        # Ignore files in our ignore patterns
        ignore_patterns = getattr(settings, 'SYNCSTATIC_IGNORE_PATTERNS', None)
        files = set(utils.get_files(local_storage, ignore_patterns=ignore_patterns))

        # Remove any files that went into compilation
        files -= set(settings.PIPELINE_JS['main']['source_filenames'])
        files -= set(settings.PIPELINE_CSS['main']['source_filenames'])

        for file in files:
            print "syncing to s3: %s" % file
            staticfiles_storage.save(file, local_storage.open(file, 'r'))
