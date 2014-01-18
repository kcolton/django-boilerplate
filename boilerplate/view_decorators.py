import csv
import json
import functools

from django.http import HttpResponse, HttpResponseServerError
from django.conf import settings

from .view_shortcuts import render_html

CONTENT_TYPE_JSON = 'application/json; charset=utf-8'
CONTENT_TYPE_CSV = 'text/csv'


def json_view(view_func=None, allow_jsonp=False):

    if view_func is None:
        return functools.partial(json_view, allow_jsonp=allow_jsonp)

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):

        try:
            output = view_func(request, *args, **kwargs)
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

        try:
            json_string = json.dumps(output)
        except TypeError:
            # Not serializable, perhaps something like a redirect. Just return
            return output

        if allow_jsonp and 'callback' in request.GET:
            json_string = '%s(%s)' % (request.GET['callback'], json_string)

        return response_class(json_string, content_type=CONTENT_TYPE_JSON)
    return wrapper


def html_view(view_func=None, template=None, response_class=None):
    """
    Decorates a dictionary returning view into one that returns a rendered template into an HttpResponse
    Optional constructor params: template=, a template to use, a little cleaner than the dictionary key,
    but not always applicable. A single view function may return different templates depending on the logic
    """
    if view_func is None:
        return functools.partial(html_view, template=template, response_class=response_class)

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        context = view_func(request, *args, **kwargs) or dict()

        if not isinstance(context, dict):
            # Todo allow Django context object?
            # Return from function is not a dict? Can't do anything with it, just return it
            return context

        # Use the dictionary TEMPLATE if present, or use the one given in constructor
        tpl = context.pop('TEMPLATE', template)
        response = render_html(request, tpl, context=context, response_class=response_class)

        return response

    return wrapper


def csv_attachment_view(view_func=None, filename='spreadsheet.csv'):
    if view_func is None:
        return functools.partial(csv_attachment_view, filename=filename)

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        output = view_func(request, *args, **kwargs)

        try:
            response = HttpResponse(content_type=CONTENT_TYPE_CSV)
            # Todo - Cleanup filename scrubbing
            response['Content-Disposition'] = 'attachment; filename="%s"' % filename.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")

            writer = csv.writer(response)
            for row in output:
                writer.writerow(row)

        except TypeError:
            # View output was not iterable. Just return whatever it was
            return output

        return response

    return wrapper