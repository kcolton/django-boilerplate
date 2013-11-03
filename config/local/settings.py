from config.common.settings import *

ENV = 'local'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'data', 'db.sqlite'),
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

