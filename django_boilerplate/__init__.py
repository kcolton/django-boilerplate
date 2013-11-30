
import datetime

from django.conf import settings


# Todo - ???
def get_title(subtitle=None):
    return '%s - %s' % (settings.TITLE, subtitle) if subtitle else settings.TITLE


def context_processor(request):
    return {
        'request': request,
        'GET': request.GET,
        'POST': request.POST,

        'ENV': settings.ENV,
        'RELEASE_NUM': settings.RELEASE_NUM,

        'STATIC_URL': settings.STATIC_URL,
        'MEDIA_URL': settings.MEDIA_URL,

        'DATE': datetime.datetime.now(),

        'DEBUG': 'shitisfucked' in request.COOKIES,
        'PIPELINE_ENABLED': settings.PIPELINE_ENABLED
    }



