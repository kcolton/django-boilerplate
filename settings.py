import importlib
import os

config_settings = 'config.%s.settings' % os.environ['APP_CONFIG']
print "importing settings: %s" % config_settings

# todo - gross gross gross gross
module = __import__(config_settings, globals(), locals(), ['*'])
for k in dir(module):
    locals()[k] = getattr(module, k)