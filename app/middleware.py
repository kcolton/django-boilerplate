from urlparse import parse_qs, urlunsplit, urlsplit
from urllib import urlencode
from django.conf import settings


class AppMiddleware(object):

    def process_request(self, request):
        request.IS_BARE = '_bare' in request.REQUEST

    def process_response(self, request, response):

        response['X-Release'] = settings.RELEASE_NUM
        response['X-Request-Path'] = request.get_full_path()

        if not response.has_header('X-Title'):
            response['X-Title'] = settings.TITLE

        if hasattr(request, 'IS_BARE') and request.IS_BARE and 'Location' in response:

            # Todo - this parsing seems messy for the python world. Probably something better out there. URLObject?
            url = urlsplit(response['location'])

            if not url.scheme:  # Relative URL, add the _bare marker
                qs = parse_qs(url.query)
                qs['_bare'] = 'true'

                url = url._replace(query=urlencode(qs))
                response['Location'] = urlunsplit(url)


        return response