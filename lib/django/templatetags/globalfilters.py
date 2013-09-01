from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.timezone import get_current_timezone

register = template.Library()


@register.filter
def static(path):
    return staticfiles_storage.url(path)


@register.filter
def localtime(dt):
    return dt.astimezone(get_current_timezone())