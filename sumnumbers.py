"""
Given an array A of size N, find all combination of four elements in the array whose sum is equal to a given value K. For example, if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and K = 23, one of the quadruple is “3 5 7 8” (3 + 5 + 7 + 8 = 23).

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of input contains two integers N and K. Then in the next line are N space separated values of the array.

Output:
For each test case in a new line print all the quadruples present in the array separated by space which sums up to value of K. Each quadruple is unique which are separated by a delimeter "$" and are in increasing order.

Constraints:
1<=T<=100
1<=N<=100
-1000<=K<=1000
-100<=A[]<=100

Example:
Input:
2
5 3
0 0 2 1 1 
7 23
10 2 3 4 5 7 8
Output:
0 0 1 2 $
2 3 8 10 $2 4 7 10 $3 5 7 8 $
"""

#code
import sys

def f(a, m, k):
    sol = []
    d = {}
    for i in range(m):
        for j in range(i+1, m):
            for y in range(j+1, m):
                for z in range(y+1, m):
                    if (a[i] + a[j] + a[y] + a[z] == k):
                        quple = [a[z], a[y], a[j], a[i]]
                        quple.sort()
                        sq = ' '.join(list(map(str, quple))) + " $"
                        if sq not in d:
                            sol.append(quple)
                            d[sq] = True
    sol.sort()
    sol = [ (' '.join(list(map(str, qa))) + " $")  for qa in sol]
    return ''.join(sol) or -1


n = int(sys.stdin.readline())
for i in range(n):
    m, k = list(map(int ,sys.stdin.readline().split()))
    a = list(map(int ,sys.stdin.readline().split()))
    print(f(a, m, k))