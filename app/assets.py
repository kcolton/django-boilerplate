from django_assets import Bundle, register
from django.conf import settings

js_filters = ['yui_js']
css_filters = []

if not settings.ASSETS_DEBUG:
    css_filters.extend(['less', 'cssrewrite'])

register('main.js', Bundle(
    'js/ext/jquery/jquery.history.js',
    'js/ext/jquery/jquery.cookie.js',
    'js/ext/jquery/jquery.form.js',

    'js/ext/modernizr.js',
    'js/ext/bootstrap.js',
    'js/ext/URI.js',
    'js/ext/moment.js',

    'js/utils/Functions.js',

    'js/namespace.js',

    'js/controllers/View.js',
    'js/controllers/Page.js',
    'js/controllers/App.js',
    'js/behaviors/hijax.js',
    'js/behaviors/ui.js',

    'js/views/Home.js',

    filters=js_filters,
    output='dist/main.js'
))

register('main.css', Bundle(
    'css/main.less',

    output='dist/main.css',
    filters=css_filters,
    extra={'rel': 'stylesheet/less' if settings.ASSETS_DEBUG else 'stylesheet'}
))