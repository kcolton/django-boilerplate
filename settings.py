import importlib
import os

from config.common.settings import *

config_settings = 'config.%s.settings' % os.environ['APP_CONFIG']
importlib.import_module(config_settings)
