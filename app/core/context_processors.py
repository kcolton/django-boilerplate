from django.conf import settings

import datetime


def request(request):
    return {
        'request': request,
        'GET': request.GET,
        'POST': request.POST,
        
        'ENV': settings.ENV,
        'TITLE': settings.TITLE,
        'RELEASE_NUM': settings.RELEASE_NUM,
        'IS_BARE': request.IS_BARE,
        
        'STATIC_URL': settings.STATIC_URL,
        'MEDIA_URL': settings.MEDIA_URL,

        'DATE': datetime.datetime.now(),
        
        'DEBUG': 'shitisfucked' in request.COOKIES,
        'ASSETS_DEBUG': settings.ASSETS_DEBUG
    }