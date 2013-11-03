from django.conf import settings
from coffin.template import add_to_builtins


add_to_builtins('lib.django.templatetags.globalfilters')

# Todo - ???
def get_title(subtitle=None):
    return '%s - %s' % (settings.TITLE, subtitle) if subtitle else settings.TITLE