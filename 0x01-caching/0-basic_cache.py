#!/usr/bin/python3
"""0-basic_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Caches data. """

    def put(self, key, item):
        """Adds data to the cache. """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Gets data from the cache. """
        return self.cache_data.get(key) if key else None
