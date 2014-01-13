import os

from django.contrib.staticfiles.storage import StaticFilesStorage, staticfiles_storage
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        local_storage = StaticFilesStorage()
        base_path = local_storage.base_location

        def gather_files(rel_path=''):
            gathered_files = []
            directories, files = local_storage.listdir(rel_path)
            gathered_files += [os.path.join(rel_path, f) for f in files]

            for directory in directories:
                gathered_files += gather_files(os.path.join(rel_path, directory))

            return gathered_files

        files = gather_files()

        for file in files:
            print "syncing to s3: %s" % file
            staticfiles_storage.save(file, local_storage.open(file, 'r'))






