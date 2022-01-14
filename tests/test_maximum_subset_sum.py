import unittest
from maximum_subset_sum import max_subset_sum, recursive_max_subset_sum


class TestMaximumSubsetSum(unittest.TestCase):
    examples = [
        ([3, 7, 4, 6, 5], 13),
        ([-1, -2, -3], 0),
        ([2, 1, 5, 8, 4], 11),
        ([3, 5, -7, 8, 10], 15),
    ]

    def test_linear_version(self):
        for inputs, result in self.examples:
            assert max_subset_sum(inputs) == result

    def test_recursive_version(self):
        for inputs, result in self.examples:
            assert recursive_max_subset_sum(inputs) == result
