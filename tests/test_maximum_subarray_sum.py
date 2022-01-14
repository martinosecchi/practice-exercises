import unittest
from maximum_subarray_sum import maximum_subarray_sum

class TestMaximumSubarraySum(unittest.TestCase):
    
    def test_linear(self):
        assert maximum_subarray_sum([1, 2, 3, 4], method="linear") == 10
        assert maximum_subarray_sum([-1, -2, -3, -4], method="linear") == -1
        assert maximum_subarray_sum([1, 1, 1, -10, 2], method="linear") == 3
        assert maximum_subarray_sum([1, 1, 1, -10, 4], method="linear") == 4 

    def test_brute_force(self):
        assert maximum_subarray_sum([1, 2, 3, 4], method="brute_force") == 10
        assert maximum_subarray_sum([-1, -2, -3, -4], method="brute_force") == -1
        assert maximum_subarray_sum([1, 1, 1, -10, 2], method="brute_force") == 3
        assert maximum_subarray_sum([1, 1, 1, -10, 4], method="brute_force") == 4

    def test_dynamic(self):
        assert maximum_subarray_sum([1, 2, 3, 4], method="dynamic") == 10
        assert maximum_subarray_sum([-1, -2, -3, -4], method="dynamic") == -1
        assert maximum_subarray_sum([1, 1, 1, -10, 2], method="dynamic") == 3
        assert maximum_subarray_sum([1, 1, 1, -10, 4], method="dynamic") == 4

