from django.core.cache.backends.memcached import MemcachedCache
from hash_ring import MemcacheRing

class ConsistentMemcachedCache(MemcachedCache):
    """
    Replaces the default memcached.Client with MemcacheRight which extends memcached.Client
    Uses consistent hashing instead of modulo
    """
    @property
    def _cache(self):
        if getattr(self, '_client', None) is None:
            self._client = MemcacheRing(self._servers)

        return self._client