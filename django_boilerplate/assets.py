from django_assets import Bundle, register
from django.conf import settings

import django_hijax.assets


JS_ASSETS = (
    'third_party/jquery/jquery.cookie.js',
    'third_party/jquery/jquery.form.js',
    'third_party/bootstrap/bootstrap.js',
    'third_party/modernizr.js',
    'third_party/moment.js',

    'djbp/js/namespace.js',
    'djbp/js/utils/Functions.js',
    'djbp/js/controllers/View.js',
    'djbp/js/controllers/App.js',
    'djbp/js/behaviors/ui.js',
    'djbp/js/views/Home.js',
) + django_hijax.assets.JS_ASSETS

STYLE_ASSETS = (
    'third_party/bootstrap/less/bootstrap.less',
    'djbp/css/main.less',
) + django_hijax.assets.STYLE_ASSETS


js_filters = ['yui_js']
css_filters = []

if not settings.ASSETS_DEBUG:
    css_filters.extend(['less', 'cssrewrite'])

register('main.js', Bundle(*JS_ASSETS, filters=js_filters, output='dist/main.js'))

register('main.css', Bundle(*STYLE_ASSETS, output='dist/main.css', filters=css_filters,
                            extra={'rel': 'stylesheet/less' if settings.ASSETS_DEBUG else 'stylesheet'}
                            ))