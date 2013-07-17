from django import template
from django.contrib.staticfiles.storage import staticfiles_storage

register = template.Library()

@register.filter
def static(path):
    return staticfiles_storage.url(path)

@register.filter
def has_attr(object, attr):
    return hasattr(object, attr)