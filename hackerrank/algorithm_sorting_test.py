# import pytest
import algorithm_sorting


class TestIntroTutorial(object):
    def test_intro_tutoral(self):
        sort1 = algorithm_sorting.Sorting()
        V = 4
        arr = [1, 4, 5, 7, 9, 12]
        result = sort1.intro_tutorial(V, arr)
        assert(result == 1)


class TestMedian(object):
    def test_median_one(self):
        sort1 = algorithm_sorting.Sorting()
        arr = [0, 1, 2, 4, 6, 5, 3]
        result = sort1.median(arr)
        assert(result == 3)


class TestInsertionSortAnalyse(object):
    def test_insertion_sort_analyse_one(self):
        sort1 = algorithm_sorting.Sorting()
        arr = [1, 1, 1, 2, 2]
        result = sort1.insertion_sort_analyse(arr)
        assert(result == 0)

    def test_insertion_sort_analyse_two(self):
        sort1 = algorithm_sorting.Sorting()
        arr = [2, 1, 3, 1, 2]
        result = sort1.insertion_sort_analyse(arr)
        assert(result == 4)

    def test_insertion_sort_analyse_three(self):
        sort1 = algorithm_sorting.Sorting()
        arr = [1, 1, 1, 2, 2]
        result = sort1.insertion_sort_analyse_two(arr)
        assert(result == 0)

    def test_insertion_sort_analyse_four(self):
        sort1 = algorithm_sorting.Sorting()
        arr = [2, 1, 3, 1, 2]
        result = sort1.insertion_sort_analyse_two(arr)
        assert(result == 4)
