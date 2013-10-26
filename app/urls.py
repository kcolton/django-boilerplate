from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core import urlresolvers
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('app.views',
    url(r'^$', 'example.index', name='home'),

    url(r'^form/$', 'example.form_example', name='form_example'),
    url(r'^messages/$', 'example.messages_example', name='messages_example'),
    url(r'^redirect-internal/$', 'example.redirect_internal', name='redirect_internal'),
    url(r'^redirect-external/$', 'example.redirect_external', name='redirect_external'),

    url(r'^foo/$', 'example.foo', name='foo'),
    url(r'^bar/$', 'example.bar', name='bar'),

    url(r'^csv-download/$', 'example.csv_download', name='csv_download_example'),

    url(r'^json/$', 'example.json', name='json_example'),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Some globally annoying URLs that we don't want django spending much time on
    # Please cache this shit out of this
    url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('app/favicon.ico'))),
)
