from config.common.settings import *

ENV = ENV_LOCAL
STORAGE = STORAGE_LOCAL


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'data/db.sqlite'),
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

