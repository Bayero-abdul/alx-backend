#!/usr/bin/python3
"""2-lifo_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Caches data. """

    def put(self, key, item):
        """Adds data to the cache. """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key = list(self.cache_data)[-2]
            self.cache_data.pop(key)
            print(f'DISCARD: {key}')

    def get(self, key):
        """Gets data from the cache. """
        return self.cache_data.get(key) if key else None
