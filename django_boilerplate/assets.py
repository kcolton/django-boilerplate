import importlib


class AppAssets(object):
    def __init__(self):
        self.js_libraries = list()
        self.js_app_scripts = list()

        self.css_libraries = list()
        self.css_app_styles = list()

    @classmethod
    def autodiscover(cls, packages):

        app_assets = AppAssets()

        for package in packages:
            try:
                assets_module = importlib.import_module('%s.assets' % package)

                try:
                    app_assets.js_libraries += list(assets_module.JS_LIBRARIES)
                except AttributeError:
                    pass

                try:
                    app_assets.js_app_scripts += list(assets_module.JS_APP_SCRIPTS)
                except AttributeError:
                    pass

                try:
                    app_assets.css_libraries += list(assets_module.CSS_LIBRARIES)
                except AttributeError:
                    pass

                try:
                    app_assets.css_app_styles += list(assets_module.CSS_APP_STYLES)
                except AttributeError:
                    pass

            except ImportError:
                pass

        return app_assets


JS_LIBRARIES = (
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

CSS_LIBRARIES = (
    'third_party/bootstrap/less/bootstrap.less',
    'djbp/css/main.less',
)