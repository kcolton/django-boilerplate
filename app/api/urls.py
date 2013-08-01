from django.conf.urls import *

urlpatterns = patterns('app.api.views',
    (r'^account/load/$', 'account.load')
)