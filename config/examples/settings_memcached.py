# Copy-paste. Do not import directly
# WARNING: This has not been used thoroughly at all yet ...

CACHES = {
    'default': {
        'BACKEND': 'lib.django.cache.memcached.ConsistentMemcachedCache',
        'LOCATION': 'localhost:11211',
        'KEY_PREFIX': ''
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
