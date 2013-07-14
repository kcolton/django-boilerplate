from django_assets import Bundle, register
from django.conf import settings

js_filters = []
css_filters = []

if not settings.ASSETS_DEBUG:
    css_filters.extend(['less', 'cssrewrite'])

register('main.js', Bundle(
    'js/ext/modernizr.js',
    'js/ext/bootstrap.js',

    'js/utils/Functions.js',

    filters=js_filters,
    output='dist/main.js'))

register('main.css', Bundle(
    'css/ext/bootstrap.css',
    'css/main.less',

    output='dist/main.css',
    filters=css_filters,
    extra={'rel': 'stylesheet/less' if settings.ASSETS_DEBUG else 'stylesheet'}
    ))