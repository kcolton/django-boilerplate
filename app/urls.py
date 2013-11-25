from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib import admin

from django_boilerplate import example_urls
from django_boilerplate.views import errors

admin.autodiscover()

urlpatterns = patterns('app.views',
    url(r'', include(example_urls)),
    url(r'^admin/', include(admin.site.urls)),

    # Some globally annoying URLs that we don't want django spending much time on
    # Please cache this shit out of this
    url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = errors.handler500
handler404 = errors.handler404
