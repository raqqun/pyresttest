import collections

# LRU cache to reduce file access
# Based on http://www.kunxi.org/blog/2014/05/lru-cache-in-python/
class LRUCache:
    cache = None
    capacity = 16

    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        """ Return stored key, or none if unstored, making the stored value most recent """
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        return None

    def put(self, key, value):
        """ Store key-value pair, evicting the oldest entry if needed """
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key]=value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)