"""
Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:

Corresponding to each test case, in a new line, print the starting and ending positions of first such occuring subarray if sum equals to subarray, else print -1.

Note: Position of 1st element of the array should be considered as 1.

Expected Time Complexity: O(n)

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100
1 ≤ an array element ≤ 200

Example:

Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10

Output:
2 4
1 5
"""

# O(n^2)
def f1(a, S):
    N = len(a)
    for i in range(N):
        for j in range(N):
            if sum(a[i:j+1]) == S:
                return i,j
    return False

# O(n) not correct
def f2(a, S):
    lo, hi = 0, len(a)-1
    while lo < hi:
        ls = sum(a[lo:hi+1])
        if ls == S:
            return lo, hi
        elif ls < S:
            return False
        else:
            # remove one or the other, by what criterion?
            # the elements by themselves don't tell me nothing unless they are sorted.
            # so I have to look fo both options
            if a[lo] <= a[hi]:
                lo += 1
            else:
                hi += -1

    return False
    
# O(n)
def f3(a, S):
    N = len(a)
    curr_sum = a[0]
    start = 0
    i = 1
    while i <= N:
        while curr_sum > S and start < i-1:
            curr_sum = curr_sum - a[start]
            start += 1

        if curr_sum == S:
            return start, i-1

        if i < N:
            curr_sum = curr_sum + a[i]
        i += 1
 
    return False

for f in (f1, f2, f3):
    print()
    print(f)
    print()

    N, S = 5, 12
    a = [1, 2, 3, 7, 5]

    print(f(a, S), (1, 3), f(a, S) == (1, 3))

    N, S = 10, 15
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f(a, S), (0, 4), f(a, S) == (0, 4))

    N, S = 10, 15
    a = [1, 1, 1, 1, 1, 6, 1, 8, 1, 1]
    print(f(a, S), (5, 7), f(a, S) == (5, 7))

    N, S = 10, 15
    a = [2, 1, 1, 0, 1, 1, 1, 6, 1, 8]
    print(f(a, S), (7, 9), f(a, S) == (7, 9))