import unittest
from median_in_stream import MedianPriorityQueue


class TestMedianPriorityQueue:

    def test_gets_new_median_continuously(self):
        median_pq = MedianPriorityQueue()
        
        median_pq.add(5)
        assert median_pq.get_median() == 5.  # 5

        median_pq.add(15)
        assert median_pq.get_median() == 10.  # 5, 15

        median_pq.add(1)
        assert median_pq.get_median() == 5.  # 1, 5, 15

        median_pq.add(3)
        assert median_pq.get_median() == 4.  # 1, 3, 5, 15
        
        median_pq.add(20)
        assert median_pq.get_median() == 5.  # 1, 3, 5, 15, 20
