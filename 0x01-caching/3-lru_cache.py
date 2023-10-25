#!/usr/bin/python3
"""3-lru_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Caches data. """

    def __init__(self):
        super().__init__()
        self.freq = {}
        self.index = 0

    def put(self, key, item):
        """Adds data to the cache. """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.freq[key] = self.index
        self.index += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            min_key = min(self.freq, key=self.freq.get)
            self.cache_data.pop(min_key)
            self.freq.pop(min_key)
            print(f'DISCARD: {min_key}')

    def get(self, key):
        """Gets data from the cache. """
        if key in self.cache_data:
            self.freq[key] = self.index
            self.index += 1

        return self.cache_data.get(key) if key else None
