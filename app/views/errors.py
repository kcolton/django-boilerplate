from django.http import HttpResponseServerError, HttpResponseNotFound
from lib.django.views.decorators import html_view


@html_view(template='errors/404.tpl', response_class=HttpResponseNotFound)
def handler404(request):
    pass


@html_view(template='errors/500.tpl', response_class=HttpResponseServerError)
def handler500(request):
    pass