import os
from django.conf.global_settings import *

SECRET_KEY = 'boilerplateinit'

PROJECT_TEMPLATE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'project_template')

INSTALLED_APPS = (
    'boilerplate'
)