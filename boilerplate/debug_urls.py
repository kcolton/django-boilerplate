from django.conf.urls import patterns, include, url

urlpatterns = patterns('boilerplate.views.debug',
    url(r'^500/$', 'error_500', name='debug_error_500'),
)
