import ujson as json
import functools
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.conf import settings
from lib.django.views.shortcuts import render_html

MIME_JSON = 'application/json; charset=utf-8'


def json_view(view_func=None, allow_jsonp=False):

    if view_func is None:
        return functools.partial(json_view, allow_jsonp=allow_jsonp)

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):

        try:
            output = view_func(request, *args, **kwargs)

            # Todo - We may receive valid json serializable non-dicts
            # Is there a better, more pythonic way of detecting other responses / json serializability?
            if not isinstance(output, dict):
                return output

        except StandardError as e:
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

        if allow_jsonp and 'callback' in request.GET:
            json_string = '%s(%s)' % (request.GET['callback'], json_string)

        return response_class(json_string, mimetype=MIME_JSON)
    return wrapper


def html_view(view_func=None, template=None):
    """
    Decorates a dictionary returning view into one that returns a rendered template into an HttpResponse
    Optional constructor params: template=, a template to use, a little cleaner than the dictionary key,
    but not always applicable. A single view function may return different templates depending on the logic
    """
    if view_func is None:
        return functools.partial(html_view, template=template)

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        output = view_func(request, *args, **kwargs)

        # Return from function is not a dict? Can't do anything with it, just return it
        if not isinstance(output, dict):
            return output

        # Use the dictionary TEMPLATE if present, or use the one given in constructor
        tpl = output.pop('TEMPLATE', template)

        return render_html(request, tpl, output)

    return wrapper



