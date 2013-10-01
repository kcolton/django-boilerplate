from config.common.settings import *

ENV = 'local'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TOP_ROOT, 'db.sqlite'),
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

