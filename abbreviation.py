#!/bin/python3
from typing import Union


# You can perform the following operations on the string, a:
# - Capitalize zero or more of a's lowercase letters.
# - Delete all of the remaining lowercase letters in a.
# Given two strings, a and b, determine if it's possible to make a equal to b as described. 
# If so, print YES on a new line. Otherwise, print NO.
#
# For example, given a = AbcDE and b = ABDE, in a we can convert b and delete c to match b. 
# If a = AbcDE and b = AFDE, matching is not possible because letters may only be capitalized or discarded, not changed.


def abbreviation(a: str, b: str) -> str:
    
    def inner(a, i) -> bool:
        # either capitalize or remove every lowercase letter in a,
        # at the end check result
        if i >= len(a):
            return remove_all_lowercase(a) == b
        if remove_all_lowercase(a[:i]) != b[:i]:
            return False

        if a[i].isupper():
            return inner(a, i+1)
        return (
            inner(to_uppercase_at_index(a, i), i+1) or
            inner(remove_char_at_index(a, i), i)
        )
        
    return "YES" if inner(a, 0) else "NO"


def to_uppercase_at_index(a: str, i: int) -> str:
    beginning = list(a[:i])
    ending = list(a[i+1:]) if i < len(a) - 1 else []
    return "".join(beginning + [a[i].upper()] + ending)


def remove_char_at_index(a: str, i: int) -> str:
    beginning = list(a[:i])
    ending = list(a[i+1:]) if i < len(a) - 1 else []
    return "".join(beginning + ending)


def next_uppercase(a: str, i: int) -> int:
    if i >= len(a) - 1:
        return len(a) - 1
    if a[i].isupper():
        return i
    return next_uppercase(a, i+1)


def remove_all_lowercase(a: str) -> str:
    return "".join([c for c in a if c.isupper()])


if __name__ == '__main__':
    assert abbreviation("HIFuOPyb", "HIFOP") == "YES"
    assert abbreviation("daBcd", "ABC") == "YES"
    assert abbreviation("beFgH", "EFH") == "YES"
    assert abbreviation("ababbaAbAB", "AABABB") == "NO"
    assert abbreviation("aAbAb", "ABAB") == "YES"
    assert abbreviation("baaBa", "BAAA") == "NO"
    assert abbreviation("abAAb", "AAA") == "YES"
    assert abbreviation("babaABbbAb", "ABAA") == "NO"
