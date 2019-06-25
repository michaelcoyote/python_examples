# import pytest
import algorithm_sorting


class TestMedian(object):
    def test_median_one(self):
        sort1 = algorithm_sorting.Sorting()
        arr = [0, 1, 2, 4, 6, 5, 3]
        result = sort1.median(arr)
        assert(result == 3)
