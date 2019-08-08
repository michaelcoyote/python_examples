#!/usr/bin/env python
"""Test a cache."""

import datetime
import random


class Cache:
    """Implement a simple key/value cache.

    This a very basic implementation of a k/v cache
    with older k/v pairs aging off as new keys are added
    and old ones are not accessed.

    Cache(max_cache_size=10)

    max_cache_size should be integer and can be adjusted on
    the fly by setting Cache.max_cache_size as needed
    """

    def __init__(self, max_cache_size=10):
        self._cache = {}
        self.max_cache_size = max_cache_size

    def __contains__(self, key):
        """Return True/False on a given key for a cache.

        This redefines class builtin __contains__."""
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

    def update(self, key, value):
        """Update and clean cache.

        Takes key and value as attributes.
        No return valute.
        """
        if (key not in self._cache and
                len(self._cache) >= self.max_cache_size):
            self.expire_oldest()
        self._cache[key] = {'date_accessed': datetime.datetime.now(),
                            'value': value}

    def get(self, key):
        """Get a value using a key.

        The Cache.get(key) method takes a key as an attribute and
        if the key exists in the cache, it will update the access time
        and return the value stored for the key.
        If the key does not exist None is returned.
        """

        if key in self:
            self._cache[key]['date_accessed'] = datetime.datetime.now()
            return self._cache[key]['value']
        else:
            return None

    def expire_oldest(self):
        """Expire oldest entry by "date_accessed".

        The Cache.expire_oldest() method takes no attributes
        and will expire the oldest entry."""
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
        """Cache size.

        The Cache.size() method takes no attributes and returns
        the number of entries in the cache."""
        return len(self._cache)


def run_cache(keys, cache, c):
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


def main():
    keys = ['foo', 'bar', 'baz', 'moo', 'vxx', 'quux', 'gack', 'florb',
            'rarg', 'boop', 'wrm', 'flum', 'mox', 'arrd']
    c = 'abcdefghijklmnop'
    cache = Cache()
    run_cache(keys, cache, c)


if __name__ == '__main__':
    main()
