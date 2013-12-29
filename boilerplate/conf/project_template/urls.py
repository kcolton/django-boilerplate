from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.contrib import admin

from boilerplate import example_urls, debug_urls
from boilerplate.views import errors

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'', include('{{ project_name }}.urls')),
    url(r'', include(example_urls)),
    url(r'^debug/', include(debug_urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    url(r'^apple-touch-icon-precomposed.png$', RedirectView.as_view(url=staticfiles_storage.url('apple-touch-icon-precomposed.png'))),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = errors.handler500
handler404 = errors.handler404
