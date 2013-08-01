from lib.django.views.decorators import HtmlView
from django.views.decorators.cache import cache_control

@cache_control(public=True, s_maxage=3600, max_age=3600)
@HtmlView(template='example/index.tpl')
def index(request):
    return {}

@cache_control(public=True, s_maxage=3600, max_age=3600)
@HtmlView(template='example/foo.tpl')
def foo(request):
    return {}

@cache_control(public=True, s_maxage=3600, max_age=3600)
@HtmlView(template='example/bar.tpl')
def bar(request):
    return {}