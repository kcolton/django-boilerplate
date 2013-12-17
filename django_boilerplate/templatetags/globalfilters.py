from dateutil import parser
from coffin import template
from django import forms
from django.utils.timezone import get_current_timezone_name
import pytz

register = template.Library()


@register.filter
def absolute_url(relative, request):
    return request.build_absolute_uri(relative)


@register.filter
def localtime(dt):
    try:
        timezone = pytz.timezone(get_current_timezone_name())
        return timezone.localize(dt) if dt.tzinfo is None else dt.astimezone(timezone)
    except AttributeError:
        return dt


@register.filter
def parsedatetime(dt_str):
    if not dt_str:
        return None

    try:
        return parser.parse(dt_str)
    except ValueError:
        return None


@register.filter
def split(to_split, *args):
    return to_split.split(*args)


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)


@register.filter
def is_radio(field):
    return isinstance(field.field.widget, forms.RadioSelect)


@register.filter
def is_checkbox_multiple(field):
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@register.filter
def is_file(field):
    return isinstance(field.field.widget, forms.FileInput)


@register.filter
def is_date(field):
    return isinstance(field.field.widget, forms.DateInput)


@register.filter
def is_datetime(field):
    return isinstance(field.field.widget, forms.DateTimeInput)


@register.filter
def classname(obj):
    return obj.__class__.__name__


@register.filter
def mailto(email):
    return '<a href="mailto:%s">%s</a>' % (email, email)