#!/bin/python3

def max_common_child(s1: str, s2: str) -> int:
    """A string is said to be a child of a another string if it can be formed by deleting 
    0 or more characters from the other string. Letters cannot be rearranged. 
    Given two strings of equal length, what's the longest string that can be constructed 
    such that it is a child of both?
    Example:
    s1 = "ABCD", s2 = "ABDC"
    common_child(s1, s2) == 3   (both "ABC" and "ABD" are valid)
    """

    memo = {}

    def memoize(func):
        def decorator(s1, s2, length=0):
            key = s1 + "-" + s2
            if key not in memo:
                memo[key] = func(s1, s2, length)
            return memo[key]
        
        return decorator    


    # O(N^2) with memoization
    # note that for large strings it can get N^2 recursions and throw a RecursionError
    @memoize
    def max_child_length_recursive(s1: str, s2: str, length: int = 0) -> int:
        if len(s1) == 0 or len(s2) == 0:
            return length

        # take the character if present in both strings and continue
        if s1[0] == s2[0]:
            return max_child_length_recursive(s1[1:], s2[1:], length + 1)

        return max(
            max_child_length_recursive(s1[1:], s2, length),  # skip one from s1
            max_child_length_recursive(s1, s2[1:], length)   # skip one from s2
        )

    # O(^2)
    def max_child_length_with_matrix(s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        if n1 == 0 or n2 == 0: 
            return 0
        
        solutions_matrix = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i-1] == s2[j-1]:
                    solutions_matrix[i][j] = solutions_matrix[i-1][j-1] + 1
                else:
                    solutions_matrix[i][j] = max(solutions_matrix[i][j-1], solutions_matrix[i-1][j])
        return solutions_matrix[n1][n2]
    

    # s1 = remove_all_from_string(s1, set(s1) - set(s2))
    # s2 = remove_all_from_string(s2, set(s2) - set(s1))
    # return max_child_length_recursive(s1, s2)

    return max_child_length_with_matrix(s1, s2)


def remove_all_from_string(s: str, characters: list) -> str:
    for c in characters:
        s = s.replace(c, "")
    return s
