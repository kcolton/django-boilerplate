import importlib


def autodiscover_assets(packages):
    js_assets = list()
    css_assets = list()

    for package in packages:
        try:
            assets_module = importlib.import_module('%s.assets' % package)

            try:
                js_assets += list(assets_module.JS_ASSETS)
            except AttributeError:
                pass

            try:
                css_assets += list(assets_module.CSS_ASSETS)
            except AttributeError:
                pass

        except ImportError:
            pass

    return js_assets, css_assets


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
)

CSS_ASSETS = (
    'third_party/bootstrap/less/bootstrap.less',
    'djbp/css/main.less',
)