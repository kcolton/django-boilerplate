from django.conf.urls import patterns, include, url

urlpatterns = patterns('app.views.example',
    url(r'^$', 'index', name='home'),

    url(r'^form/$', 'form_example', name='form_example'),
    url(r'^messages/$', 'messages_example', name='messages_example'),
    url(r'^redirect-internal/$', 'redirect_internal', name='redirect_internal'),
    url(r'^redirect-external/$', 'redirect_external', name='redirect_external'),
    url(r'^info/$', 'info', name='foo'),

    url(r'^foo/$', 'foo', name='foo'),
    url(r'^bar/$', 'bar', name='bar'),

    url(r'^csv-download/$', 'csv_download', name='csv_download_example'),
    url(r'^json/$', 'json', name='json_example'),
    url(r'^error/$', 'error', name='error_example'),
    url(r'^log/$', 'log', name='log_example'),
)
