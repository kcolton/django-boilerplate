from functools import wraps
import ujson as json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.conf import settings

MIME_JSON = 'application/json; charset=utf-8'

class JsonView(object):
    def __init__(self):
        pass

    def __call__(self, fn):
        """ Decorates a dictionary returning view into one that returns a valid json response """
        @wraps(fn)
        def wrapper(request, *args, **kwargs):

            try:
                output = fn(request, *args)

            except Exception as e:
                # Even for exception we want to return json
                # Come what may, we're returning JSON.
                output = {'error': True}
                
                # In debug mode, raise the exception
                if settings.DEBUG:
                    raise
                
                # Return json, but with a 500 status
                response_class = HttpResponseServerError
            else:
                # All went well, return normal response
                response_class = HttpResponse

            return response_class(json.dumps(output), mimetype=MIME_JSON)

        return wrapper


