from lib.django.views.decorators import HtmlView
from django.views.decorators.cache import cache_control

@cache_control(public=True, s_maxage=3600)
@HtmlView(template='index.tpl')
def index(request):
    return {}

@HtmlView(template='foo.tpl')
def foo(request):
    return {}

@HtmlView(template='bar.tpl')
def bar(request):
    return {}