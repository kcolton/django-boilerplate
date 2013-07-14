from django.conf.urls import *

urlpatterns = patterns('app.web.views',
    url(r'^$', 'index', name='home'),
)
