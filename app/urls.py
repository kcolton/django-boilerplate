from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('app.views',
    url(r'^$', 'example.index', name='home'),

    url(r'^form/$', 'example.form_example', name='form_example'),
    url(r'^messages/$', 'example.messages_example', name='messages_example'),

    url(r'^foo/$', 'example.foo', name='foo'),
    url(r'^bar/$', 'example.bar', name='bar'),

    # Uncomment this if you actually add stuff into the api sub app
    url(r'^a/', include('app.api.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Some globally annoying URLs that we don't want django spending much time on
    # Please cache this shit out of this
    url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('app/favicon.ico'))),
)
