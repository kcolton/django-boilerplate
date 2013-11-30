import django_hijax.assets


JS_ASSETS = (
    'third_party/jquery/jquery.cookie.js',
    'third_party/jquery/jquery.form.js',
    'third_party/bootstrap/bootstrap.js',
    'third_party/modernizr.js',
    'third_party/moment.js',
    'third_party/ba_debug.js',
    'third_party/URI.js',

    'djbp/js/namespace.js',
    'djbp/js/utils/Functions.js',
    'djbp/js/controllers/View.js',
    'djbp/js/controllers/App.js',
    'djbp/js/behaviors/ui.js',
    'djbp/js/views/*.js',
) + django_hijax.assets.JS_ASSETS

CSS_ASSETS = (
    'third_party/bootstrap/less/bootstrap.less',
    'djbp/css/main.less',
) + django_hijax.assets.CSS_ASSETS