from coffin import shortcuts
from django.template import RequestContext
from django.http import HttpResponse


def render_to_string(request, template, context):
    if request:
        context_instance = RequestContext(request)
    else:
        context_instance = None

    return shortcuts.render_to_string(template, context, context_instance)


def render_html(request, template, context=None, content_type='text/html', response_class=None):
    context = context or dict()
    response_class = response_class or HttpResponse

    response = render_to_string(request, template, context)
    return response_class(response, content_type=content_type)

