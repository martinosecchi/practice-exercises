from typing import List
from utils import memoize


def maximum_subarray_sum(arr: List[int], method: str = "linear") -> int:
    """Given an array containing both negative and positive integers, 
    find the contiguous sub-array with maximum sum and return the sum.
    
    Example:
    maximum_subarray_sum([1, 2, 3]) == 6
    maximum_subarray_sum([-1, -2, -3, -4]) == -1

    Arguments:
        arr: the array
        method: either of "linear" | "brute_force" | "dynamic" for the specific implementation

    Returns:
        the maximum sum of every possible contiguous subarrays
    """
    n = len(arr)

    # O(2^n -1)
    def dynamic():

        @memoize
        def _max_sum(i: int, sum: int):
            if i == n - 1:
                return max(sum, max(sum + arr[i], arr[i]))

            return max(
                _max_sum(i + 1, sum + arr[i]), 
                _max_sum(i + 1, arr[i]), 
                sum
            )

        return _max_sum(1, arr[0])


    # O(n^2)
    def brute_force():
        best = []
        for i in range(n):
            cumulative_sum = 0
            best.append(arr[i])
            for j in range(i, n):
                cumulative_sum += arr[j]
                if cumulative_sum > best[i]:
                    best[i] = cumulative_sum
        return max(best)


    # O(n)
    def linear():
        best = arr[0]
        cumulative_sum = 0
        for e in arr:
            cumulative_sum += e
            best = max(best, cumulative_sum)
            if cumulative_sum < 0:
                cumulative_sum = 0
        return best


    get_method = {
        "linear": linear,
        "brute_force": brute_force,
        "dynamic": dynamic,
    }
    return get_method[method]()
    

