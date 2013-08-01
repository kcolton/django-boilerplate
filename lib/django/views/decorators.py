import ujson as json
from functools import wraps
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.conf import settings
from lib.django.views.shortcuts import render_html

MIME_JSON = 'application/json; charset=utf-8'

class JsonView(object):
    def __init__(self, allow_jsonp=False):
        self.allow_jsonp = allow_jsonp

    def __call__(self, fn):
        """ 
        Decorates a dictionary returning view into one that returns a valid json response
        """
        @wraps(fn)
        def wrapper(request, *args, **kwargs):

            try:
                output = fn(request, *args, **kwargs)

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

            json_string = json.dumps(output)

            # If jsonp, wrap in a callback
            if self.allow_jsonp and 'callback' in request.GET:
                json_string = '%s(%s)' % (request.GET['callback'], json_string)

            return response_class(json_string, mimetype=MIME_JSON)

        return wrapper

class HtmlView(object):
    """
    Decorates a dictionary returning view into one that returns a rendered template into an HttpResponse
    Optional constructor params: template=, a template to use, a little cleaner than the dictionary key,
    but not always applicable. A single view function may return different templates depending on the logic
    """

    def __init__(self, template=None):
        self.template = template

    def __call__(self, fn):

        @wraps(fn)
        def wrapper(request, *args, **kwargs):

            output = fn(request, *args, **kwargs)

            # Return from function is not a dict? Can't do anything with it, just return it
            if not isinstance(output, dict):
                return output

            # Use the dictionary TEMPLATE if present, or use the one given in constructor
            tpl = output.pop('TEMPLATE', self.template)

            return render_html(request, tpl, output)

        return wrapper



