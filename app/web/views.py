from lib.django.views.decorators import HtmlView

@HtmlView(template='index.tpl')
def index(request):
    return {
        'foo': 'bar!'
    }