import unittest
from increment_digits_list import increment


class TestIncrementDigits(unittest.TestCase):
    
    def test_basic_increment(self):
        assert increment([1, 2, 3, 4]) == [1, 2, 3, 5]

    def test_carry_the_1(self):
        assert increment([8, 9]) == [9, 0]

    def test_carry_over_multiple_positions(self):
        assert increment([9, 9]) == [1, 0, 0]
