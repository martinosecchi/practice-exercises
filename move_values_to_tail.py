from typing import List
from utils import swap


def move_to_tail(arr: List[int], value: int) -> List[int]:
    """Move all values in arr that are equal to value to the last positions of arr.
    Disregard the other elements' positions.
    Note: original array is modified.
    """
    last = len(arr) - 1 
    i = 0
    while i < last:
        if arr[i] == value:
            swap(arr, i, last)
            last -= 1
        else:
            i += 1
    return arr


def move_to_tail_and_maintain_order(arr: List[int], value: int) -> List[int]:
    """Move all values in arr that are equal to value to the last positions of arr.
    Maintain the other elements' positions.
    Note: original array is not modified.
    """
    i = 0
    count = 0
    arr2 = []
    while i < len(arr):
        if arr[i] == value:
            count += 1
        else:
            arr2.append(arr[i])
        i += 1 
    return arr2 + ([value] * count)

