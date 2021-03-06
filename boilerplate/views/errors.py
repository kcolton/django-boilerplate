import logging

from django.http import HttpResponseServerError, HttpResponseNotFound
from hijax.view_decorators import set_title

from ..view_decorators import html_view
from .. import get_title

logger = logging.getLogger('django.request')


@set_title(get_title('Oops!'))
@html_view(template='errors/404.tpl', response_class=HttpResponseNotFound)
def handler404(request):
    logger.warning('HTTP 404 - %s - %s - "%s"' % (request.get_full_path(), request.META.get('REMOTE_ADDR'), request.META.get('HTTP_USER_AGENT')))


@set_title(get_title('Oops!'))
@html_view(template='errors/500.tpl', response_class=HttpResponseServerError)
def handler500(request):
    logger.warning('HTTP 500 - %s - %s - "%s"' % (request.get_full_path(), request.META.get('REMOTE_ADDR'), request.META.get('HTTP_USER_AGENT')))