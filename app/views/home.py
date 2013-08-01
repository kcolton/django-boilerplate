from lib.django.views.decorators import HtmlView

@HtmlView(template='index.tpl')
def index(request):
    return {}

@HtmlView(template='foo.tpl')
def foo(request):
    return {}

@HtmlView(template='bar.tpl')
def bar(request):
    return {}