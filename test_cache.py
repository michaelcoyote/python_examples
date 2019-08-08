import pytest
import cache


# Start the tests here
class TestCache(object):
    @pytest.fixture
    def cache_setup(self):
        c1 = cache.Cache(max_cache_size=2)
        for k, v in {'foo': 1, 'bar': 2}.items():
            c1.update(k, v)
        return c1

    def test_in_cache(self, cache_setup):
        """Test template"""
        assert('foo' in cache_setup)

    def test_get_hit_from_cache(self, cache_setup):
        assert(cache_setup.get('bar') == 2)

    def test_get_miss_from_cache(self, cache_setup):
        assert(cache_setup.get('does_not_exist') is None)

    def test_not_in_cache(self, cache_setup):
        assert('baz' not in cache_setup)

    def test_cache_size(self, cache_setup):
        assert(cache_setup.size == 2)

    def test_force_cache_expiration(self, cache_setup):
        for k, v in {'baz': 3, 'quux': 4, 'qux': 5}.items():
            cache_setup.update(k, v)
        print(cache_setup._cache)
        assert('foo' not in cache_setup)

    def test_set_cache(self, cache_setup):
        cache_setup.max_cache_size = 5
        assert(cache_setup.max_cache_size == 5)

    @pytest.mark.parametrize("size, error", [(-1, ValueError),
                                             ("10", TypeError)])
    def test_set_cache_invalid(self, cache_setup, size, error):
        with pytest.raises(error):
            cache_setup.max_cache_size = size
