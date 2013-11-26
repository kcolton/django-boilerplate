from ..common import environments
from ..common.settings import *

ENV = environments.ENV_LOCAL
STORAGE = environments.STORAGE_LOCAL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'data/db.sqlite'),
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

