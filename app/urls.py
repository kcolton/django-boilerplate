from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('app.views',
    url(r'', include('app.urls_example')),
    url(r'^admin/', include(admin.site.urls)),

    # Some globally annoying URLs that we don't want django spending much time on
    # Please cache this shit out of this
    url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('app/favicon.ico'))),
)

handler500 = 'app.views.errors.handler500'
handler404 = 'app.views.errors.handler404'
