import unittest
from move_values_to_tail import move_to_tail, move_to_tail_and_maintain_order


class TestMoveToTail(unittest.TestCase):
    
    def test_without_order(self):
        assert move_to_tail([1,1,2,1,3,1], 1) == [3,2,1,1,1,1]
        assert move_to_tail([2,1,3,1,1], 1) == [2,3,1,1,1]
        assert move_to_tail([3,2,1,1], 1) == [3,2,1,1]

    def test_with_order(self):
        assert move_to_tail_and_maintain_order([1,1,2,1,3,1], 1) == [2,3,1,1,1,1]
        assert move_to_tail_and_maintain_order([2,1,3,1,1], 1) == [2,3,1,1,1]
        assert move_to_tail_and_maintain_order([3,2,1,1], 1) == [3,2,1,1]
