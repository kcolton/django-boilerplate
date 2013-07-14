from coffin import shortcuts
from django.template import RequestContext
from django.http import HttpResponse

def render_to_string(request, template, context):
    if request:
        context_instance = RequestContext(request)
    else:
        context_instance = None

    return shortcuts.render_to_string(template, context, context_instance)

def render_html(request, template, context={}, mimetype='text/html'):
    response = render_to_string(request, template, context)
    return HttpResponse(response, mimetype=mimetype)

