import os
import pymysql

from django_boilerplate import configs

pymysql.install_as_MySQLdb()


class AppBase(configs.Base):
    APP_NAME = 'djbp'
    RELEASE_NUM = 2

    TITLE = 'My DJBP Application'

    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    APP_ROOT = os.path.join(PROJECT_ROOT, 'app')

    WSGI_APPLICATION = 'wsgi.application'
    ROOT_URLCONF = 'app.urls'
    AUTH_USER_MODEL = 'django_boilerplate.User'

    TIME_ZONE = 'America/New_York'
    LANGUAGE_CODE = 'en-us'

    @classmethod
    def setup(cls):
        print "AppBase - setup"
        super(AppBase, cls).setup()
        cls.INSTALLED_APPS += ('app', )


class Local(AppBase):
    ENV = configs.ENV_LOCAL
    STORAGE = configs.STORAGE_LOCAL


class LocalCompress(configs.CompressAssets, Local):
    pass


class Dev(configs.S3Assets, configs.CompressAssets, AppBase):
    ENV = configs.ENV_DEV
    STORAGE = configs.STORAGE_DEV


class Prod(configs.S3Assets, configs.CompressAssets, AppBase):
    ENV = configs.ENV_PROD
    STORAGE = configs.STORAGE_PROD

    # add jinja2 options


class Stage(Prod):
    ENV = configs.ENV_STAGE
