from typing import List


def increment(digits: List[int]) -> List[int]:
    """Given an array where all its values are integers 0-9 representing each digit of a number,
    perform an increment by 1.
    Note: the original array is modified.
    """
    i = len(digits) - 1
    carry_increment = True
    while i >= 0 and carry_increment:
        result = digits[i] + 1
        carry_increment = result > 9
        if carry_increment:
            result = result % 10
        digits[i] = result
        i -= 1

    if carry_increment:
        digits = [1] + digits

    return digits
