from django.conf.urls import patterns, url


urlpatterns = patterns('{{ project_name }}.views',
    url(r'^/$', 'home', name='home'),
)