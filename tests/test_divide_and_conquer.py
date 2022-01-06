import unittest
from algorithm_design.divide_and_conquer import find_p, find_max_profit, mergesort, mergesort_inplace


class TestExercise1(unittest.TestCase):
    
    def test_finds_p(self):
        assert find_p([1, 2, 3, 4, 5, 4, 3]) == 4

    def test_finds_first(self):
        assert find_p([5, 4, 3, 2, 1]) == 0

    def test_find_last(self):
        assert find_p([1, 2, 3, 4, 5]) == 4


class TestExercise2(unittest.TestCase):

    def test_brute_force_approach(self):
        brute, _, _ = find_max_profit([4, 3, 2, 5, 1000, 1, 10])
        i, j, profit = brute
        assert (i, j, profit) == (2, 4, 998)
        
        brute, _, _ = find_max_profit([5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1])
        i, j, profit = brute
        assert (i, j, profit) == (4, 8, 4)
        
        brute, _, _ = find_max_profit([50, 42, 49, 20, 10, 32, 20, 14, 45, 40, 43, 42, 1])
        i, j, profit = brute
        assert (i, j, profit) == (4, 8, 35)
        
        brute, _, _ = find_max_profit([9, 1, 5])
        i, j, profit = brute
        assert (i, j, profit) == (1, 2, 4)
        
        brute, _, _ = find_max_profit([0, 10, 5])
        i, j, profit = brute
        assert (i, j, profit) == (0, 1, 10)
        
        brute, _, _ = find_max_profit([100, 110, 0, 100, 5])
        i, j, profit = brute
        assert (i, j, profit) == (2, 3, 100)
        
        brute, _, _ = find_max_profit([100, 98, 100, 110, 96, 99, 100])
        i, j, profit = brute
        assert (i, j, profit) == (1, 3, 12)

    def test_divide_and_conquer_approach(self):
        _, dnq, _ = find_max_profit([4, 3, 2, 5, 1000, 1, 10])
        i, j, profit = dnq
        assert (i, j, profit) == (2, 4, 998)
        
        _, dnq, _ = find_max_profit([5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1])
        i, j, profit = dnq
        assert (i, j, profit) == (4, 8, 4)
        
        _, dnq, _ = find_max_profit([50, 42, 49, 20, 10, 32, 20, 14, 45, 40, 43, 42, 1])
        i, j, profit = dnq
        assert (i, j, profit) == (4, 8, 35)
        
        _, dnq, _ = find_max_profit([9, 1, 5])
        i, j, profit = dnq
        assert (i, j, profit) == (1, 2, 4)
        
        _, dnq, _ = find_max_profit([0, 10, 5])
        i, j, profit = dnq
        assert (i, j, profit) == (0, 1, 10)
        
        _, dnq, _ = find_max_profit([100, 110, 0, 100, 5])
        i, j, profit = dnq
        assert (i, j, profit) == (2, 3, 100)
        
        _, dnq, _ = find_max_profit([100, 98, 100, 110, 96, 99, 100])
        i, j, profit = dnq
        assert (i, j, profit) == (1, 3, 12)

    def test_optional_dynamic_programming_approach(self):
        _, _, dp = find_max_profit([4, 3, 2, 5, 1000, 1, 10])
        i, j, profit = dp
        assert (i, j, profit) == (2, 4, 998)
        
        _, _, dp = find_max_profit([5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1])
        i, j, profit = dp
        assert (i, j, profit) == (4, 8, 4)
        
        _, _, dp = find_max_profit([50, 42, 49, 20, 10, 32, 20, 14, 45, 40, 43, 42, 1])
        i, j, profit = dp
        assert (i, j, profit) == (4, 8, 35)
        
        _, _, dp = find_max_profit([9, 1, 5])
        i, j, profit = dp
        assert (i, j, profit) == (1, 2, 4)
        
        _, _, dp = find_max_profit([0, 10, 5])
        i, j, profit = dp
        assert (i, j, profit) == (0, 1, 10)
        
        _, _, dp = find_max_profit([100, 110, 0, 100, 5])
        i, j, profit = dp
        assert (i, j, profit) == (2, 3, 100)
        
        _, _, dp = find_max_profit([100, 98, 100, 110, 96, 99, 100])
        i, j, profit = dp
        assert (i, j, profit) == (1, 3, 12)


class TestMergeSort(unittest.TestCase):

    def test_sorts_correctly(self):
        assert mergesort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]
        assert mergesort([5, 3, 1, 4, 2, 6]) == [1, 2, 3, 4, 5, 6]

    def test_empty_list(self):
        assert mergesort([]) == []
        assert mergesort_inplace([]) == []

    def test_inplace_sorting(self):
        a = [5, 3, 1, 4, 2, 6]
        mergesort_inplace(a)
        assert a == [1, 2, 3, 4, 5, 6]
