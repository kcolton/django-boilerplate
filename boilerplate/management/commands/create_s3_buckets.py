from django.core.management import BaseCommand
from django.conf import settings

import boto


class Command(BaseCommand):
    def handle(self, *args, **options):
        conn = boto.connect_s3()
        conn.create_bucket(settings.AWS_STORAGE_BUCKET_NAME, policy='public-read')





