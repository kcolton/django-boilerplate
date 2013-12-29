import os
import pymysql

from boilerplate.conf import configs

pymysql.install_as_MySQLdb()


class AppBase(configs.Base):
    APP_NAME = '{{ project_name }}'
    RELEASE_NUM = 1

    TITLE = '{{ project_name }}'

    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

    WSGI_APPLICATION = 'wsgi.application'
    ROOT_URLCONF = 'urls'
    AUTH_USER_MODEL = '{{ project_name }}.User'

    TIME_ZONE = 'America/New_York'
    LANGUAGE_CODE = 'en-us'

    @classmethod
    def setup(cls):
        super(AppBase, cls).setup()
        cls.INSTALLED_APPS = ('{{ project_name }}', ) + cls.INSTALLED_APPS


class Local(AppBase):
    ENV = configs.ENV_LOCAL
    STORAGE = configs.STORAGE_LOCAL

    DEBUG = TEMPLATE_DEBUG = True


class LocalCompress(configs.CompressAssets, Local):
    pass


class LocalNoDebug(Local):
    DEBUG = TEMPLATE_DEBUG = False


class Dev(configs.S3Assets, configs.CompressAssets, AppBase):
    ENV = configs.ENV_DEV
    STORAGE = configs.STORAGE_DEV

    DEBUG = TEMPLATE_DEBUG = True


class Prod(configs.S3Assets, configs.CompressAssets, AppBase):
    ENV = configs.ENV_PROD
    STORAGE = configs.STORAGE_PROD

    DEBUG = TEMPLATE_DEBUG = False
    # add jinja2 options


class Stage(Prod):
    ENV = configs.ENV_STAGE
