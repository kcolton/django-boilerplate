import logging

from django.conf import settings


# Todo - ???
def get_title(subtitle=None):
    return '%s - %s' % (settings.TITLE, subtitle) if subtitle else settings.TITLE


logger = logging.getLogger(__name__)
