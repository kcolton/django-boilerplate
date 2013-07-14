from django.conf import settings

class CoreMiddleware(object):
    def process_response(self, request, response):
        response['X-Rel-Num'] = settings.RELEASE_NUM
        return response