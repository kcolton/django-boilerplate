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


@register.filter
def is_checkbox(field):
    return classname(field.field.widget) == 'CheckboxInput'


@register.filter
def is_radio(field):
    return classname(field.field.widget) == 'RadioSelect'


@register.filter
def is_checkbox_multiple(field):
    return classname(field.field.widget) == 'CheckboxSelectMultiple'


@register.filter
def classname(obj):
    return obj.__class__.__name__