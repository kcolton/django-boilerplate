import datetime

from django.conf import settings


def context_processor(request):
    return {
        'request': request,
        'GET': request.GET,
        'POST': request.POST,

        'ENV': settings.ENV,
        'RELEASE_NUM': settings.RELEASE_NUM,

        'STATIC_URL': settings.STATIC_URL,
        'MEDIA_URL': settings.MEDIA_URL,

        'GOOGLE_TAG_MANAGER_CONTAINER': settings.GOOGLE_TAG_MANAGER_CONTAINER,

        'DATE': datetime.datetime.now(),

        'JQUERY_UI': settings.JQUERY_UI,
        'LODASH': settings.LODASH,
        'CDN_LIBRARIES': settings.CDN_LIBRARIES,
        'PIPELINE_ENABLED': settings.PIPELINE_ENABLED
    }