from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
import urllib

register = template.Library()

@register.filter
def static(path):
    return staticfiles_storage.url(path)

@register.filter
def has_attr(object, attr):
    return hasattr(object, attr)

@register.filter
def url_escape(str):
    return urllib.quote(str)

@register.filter
def url_escape_plus(str):
    return urllib.quote_plus(str)

@register.filter
def url_encode(query):
    return urllib.urlencode(query)