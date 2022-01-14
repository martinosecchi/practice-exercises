from typing import List
from functools import lru_cache


def compare(a, b) -> int:
    """Compare two values a and b.
    """
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


def swap(arr: List, i: int, j: int):
    """Swap elements at indexes i and j inside array arr.
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def memoize(func):
    """An alias for functools.lru_cache to be used as a decorator.
    Implements memoization of the function results given the same starting argument.
    """
    return lru_cache(func)
