import unittest
from lru_cache import LRUCache

class LRUCacheTest(unittest.TestCase):

    def test_get_put(self):
        cache = LRUCache()
        cache.put(1,1)
        self.assertEqual(1, cache.get(1))

    def test_eviction(self):
        cache = LRUCache(capacity=4);

        for x in xrange(1, 100):
            cache.put(1, 'stored')
            cache.put(2, x)
            cache.put(3, x)
            cache.put(4, x)
            self.assertEqual('stored', cache.get(1))
            cache.put(5, x)
            self.assertTrue(cache.get(2) is None)

if __name__ == '__main__':
    unittest.main()