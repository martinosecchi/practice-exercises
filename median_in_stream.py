from queue import PriorityQueue, Empty


class MedianPriorityQueue:
    """
    Given an input stream of n integers > 0 the task is to insert integers to stream
    and print the median of the new stream formed by each insertion of x to the stream.

    Example:

    Flow in stream : 5, 15, 1, 3 
    5 goes to stream --> median 5 (5)
    15 goes to stream --> median 10 (5, 15)
    1 goes to stream --> median 5 (5, 15, 1)
    3 goes to stream --> median 4 (5, 15, 1, 3)
    """

    def __init__(self):
        """Keep two priority queues, one to keep the lower 50% of values (returning the highest when asked) 
        and another to keep the higher 50% of values (returning the lowest when asked).
        The median will be either the highest of the bottom 50%, the lowest of the top 50%, or an average of the two 
        depending on the size of the two queues.
        """
        self.left_pq = PriorityQueue()  # left half,  max priority queue
        self.right_pq = PriorityQueue() # right half, min priority queue

    def add(self, elem):
        """Add an element to the priority queue.
        Maintain the two left and right priority queues so that they have about the same size
        """
        left_size = self.left_pq.qsize()
        right_size = self.right_pq.qsize()
        
        left = self._get_left()
        right = self._get_right()

        if left_size == right_size:
            self._add_right(right)
            self._add_left(left)
            if elem <= left:
                self._add_left(elem)
            else:
                self._add_right(elem)

        elif left_size > right_size:
            self._add_right(right)
            if elem <= left:
                self._add_left(elem)
                self._add_right(left)
            else:
                self._add_right(elem)
                self._add_left(left)

        elif left_size < right_size:
            self._add_left(left)
            if elem <= left:
                self._add_left(elem)
                self._add_right(right)
            else:
                self._add_right(elem)
                self._add_left(right)

    def _add_left(self, elem: int) -> int:
        if elem and elem > 0:
            self.left_pq.put_nowait(-elem)
        return elem

    def _get_left(self) -> int:
        try:
            return -1 * self.left_pq.get_nowait()
        except Empty:
            return 0

    def _add_right(self, elem: int) -> int:
        if elem and elem > 0:
            self.right_pq.put_nowait(elem)
        return elem

    def _get_right(self) -> int:
        try:
            return self.right_pq.get_nowait()
        except Empty:
            return 0

    def _peek_left(self) -> int:
        return self._add_left(self._get_left())

    def _peek_right(self) -> int:
        return self._add_right(self._get_right())

    def get_median(self) -> float:
        """Return the median of the current set of values.
        The median will be either the highest value of the left queue, the lowest of the right, 
        or an average of the two depending on the size of the two queues."""
        left_size = self.left_pq.qsize()
        right_size = self.right_pq.qsize()
        
        if left_size > right_size:
            median = self._peek_left()
        elif right_size > left_size:
            median = self._peek_right()
        else:
            left = self._peek_left()
            right = self._peek_right()
            median = (left + right) / 2.0
    
        return float(median)

    def print(self):
        left = []
        right = []
        while self.left_pq.qsize() > 0:
            left.append(self._get_left())
        while self.right_pq.qsize() > 0:
             right.append(self._get_right())
        print("left: {}  right: {}".format(left, right))

        for l in left:
            self.left_pq.put_nowait(-l)
        for r in right:
            self.right_pq.put_nowait(r)

def test():
    fm = MedianPriorityQueue()
    print("-- adding {} --".format(5))
    fm.add(5)
    print("median: {}  - {}  {}".format(fm.median(), 5, fm.median() == float(5)))
    print("-- adding {} --".format(15))
    fm.add(15)
    print("median: {}  - {}  {}".format(fm.median(), 10, fm.median() == float(10)))
    print("-- adding {} --".format(1))
    fm.add(1 )
    print("median: {}  - {}  {}".format(fm.median(), 5, fm.median() == float(5)))
    print("-- adding {} --".format(3))
    fm.add(3)
    print("median: {}  - {}  {}".format(fm.median(), 4, fm.median() == float(4)))

if __name__ == '__main__':
    test()