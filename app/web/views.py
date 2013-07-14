from lib.django.views.shortcuts import render_html

def index(request):
    return render_html(request, 'index.tpl')