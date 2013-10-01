from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def check_sanity():
    """
    Look for red flags in the Django setup
    """
    if not settings.DEBUG and settings.SECRET_KEY == settings.DEFAULT_SECRET_KEY:
        raise ImproperlyConfigured('Unique SECRET_KEY required when DEBUG=False')

