#!/usr/bin/env python
"""Test a cache."""

import datetime
import random


class Cache:
    """Define a simple cache."""

    def __init__(self):
        self.cache = {}
        self.max_cache_size = 10

    def __contains__(self, key):
        """Return a T/F given a key for a cache."""
        return key in self.cache

    def update(self, key, value):
        """Update and clean cache."""
        if (key not in self.cache and 
            len(self.cache) >= self.max_cache_size):
            self.expire_oldest()
        self.cache[key] = {'date_accessed': datetime.datetime.now(),
                           'value': value}

    def expire_oldest(self):
        """Expire oldest entry."""
        oldest_entry = None
        for key in list(self.cache):
            if oldest_entry is None:
                oldest_entry = key
            elif (self.cache[key]['date_accessed'] <
                  self.cache[oldest_entry]['date_accessed']):
                print 'Removing cache entry: {}'.format(oldest_entry)
                self.cache.pop(oldest_entry)
                oldest_entry = None

    @property
    def size(self):
        """Cache size."""
        return len(self.cache)

def main():
    keys = ['foo', 'bar', 'baz', 'moo', 'vxx', 'quxx', 'gack', 'florb',
            'rarg', 'boop', 'wrm', 'flum', 'mox', 'arrd']
    c = 'abcdefghijklmnop'
    cache = Cache()
    for i, key in enumerate(keys):
        if key in cache:
            continue
        else:
            value = ' '.join([random.choice(c) for i in range(20)])
            cache.update(key,value)
        print '{} iterations, {} cached entries'.format( i+1, cache.size)
    print

if __name__ == '__main__':
    main()
