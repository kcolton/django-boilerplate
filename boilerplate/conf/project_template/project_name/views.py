from boilerplate.view_decorators import json_view, html_view


@json_view
def home(request):
    return dict(home='there is no place like it')