#!/usr/bin/env python
"""Test a cache."""

import datetime
import random


class Cache:
    """Implement a simple cache.

    Cache(max_cache_size=10)

    cache size should be integer
    """

    def __init__(self, max_cache_size=10):
        self._cache = {}
        self.max_cache_size = max_cache_size

    def __contains__(self, key):
        """Return a T/F given a key for a cache."""
        return key in self._cache

    @property
    def max_cache_size(self):
        return self._max_cache_size

    @max_cache_size.setter
    def max_cache_size(self, max):
        if max > 0:
            self._max_cache_size = max
        else:
            raise ValueError("max_cache_size needs to be greater than zero")

        return self._max_cache_size

    def update(self, key, value):
        """Update and clean cache."""
        if (key not in self._cache and
                len(self._cache) >= self.max_cache_size):
            self.expire_oldest()
        self._cache[key] = {'date_accessed': datetime.datetime.now(),
                            'value': value}

    def expire_oldest(self):
        """Expire oldest entry."""
        oldest_entry = None
        for key in list(self._cache):
            if oldest_entry is None:
                oldest_entry = key
            elif (self._cache[key]['date_accessed'] >
                  self._cache[oldest_entry]['date_accessed']):
                print('Removing cache entry: {}'.format(oldest_entry))
                self._cache.pop(oldest_entry)
                oldest_entry = None

    @property
    def size(self):
        """Cache size."""
        return len(self._cache)


def main():
    keys = ['foo', 'bar', 'baz', 'moo', 'vxx', 'quux', 'gack', 'florb',
            'rarg', 'boop', 'wrm', 'flum', 'mox', 'arrd']
    c = 'abcdefghijklmnop'
    cache = Cache()
    for i, key in enumerate(keys):
        if key in cache:
            continue
        else:
            value = ' '.join([random.choice(c) for i in range(30)])
            cache.update(key, value)
        print('{} iterations, {} keys, {} cached entries'.format(i+1,
                                                                 len(keys),
                                                                 cache.size))
    print


if __name__ == '__main__':
    main()
