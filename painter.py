"""
Dilpreet wants to paint his dog Buzo's home that has n boards with different lengths[A1, A2,..., An]. 
He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board.
The problem is to find the minimum time to get this job done under the constraints that any painter will only paint continuous sections of boards, 
say board {2, 3, 4} or only board {1} or nothing, but not board {2, 4, 5}.

Input:
The first line consists of a single integer T, the number of test cases. 
For each test case, the first line contains an integer k denoting the number of painters and integer n denoting the number of boards. 
Next line contains n- space separated integers denoting the size of boards.

Output:
For each test case, the output is an integer displaying the minimum time for painting that house.

Constraints:
1<=T<=100
1<=k<=30
1<=n<=50
1<=A[i]<=500

Example:
Input:
2
2 4
10 10 10 10
2 4
10 20 30 40
Output:
20
60
"""

def naive(a, k):
    fair = sum(a)/k
    ks = [0] * k
    curr = 0
    for piece in a:
        if curr < k-1:
            if ks[curr] >= fair:
                curr += 1
        ks[curr] += piece
    return max(ks)


def exponential(a, k):
    def f(a, k, i, C, M):
        if i >= len(a):
            return M
        if k == 0:
            C += a[i]
            M = max(M, C)
            return f(a, k, i+1, C, M)
        C += a[i]
        m = min(
            f(a, k,     i+1, C,     max(M, C)),
            f(a, k-1,   i+1, a[i],  max(M, a[i]))
            )
        return m
    return f(a, k-1, i=0, C=0, M=0)

def memoized(a, k):
    N = len(a)
    memo = {}

    def index(i,j):
        return i * N + j
    
    def f(a, k, i, C, M):
        if i >= len(a):
            # got to the end
            return M
        if k == 0:
            # painters are finished, assign to current
            C += a[i]
            M = max(M, C)            
            return f(a, k, i+1, C, M)
        #return best combination, either assign to current or to next
        C += a[i]
        if memo.get(index(k,i)) is None or (memo.get(index(k,i)) and M < memo[index(k,i)]):
            memo[index(k,i)] = min(
                f(a, k,     i+1, C,     max(M, C)),
                f(a, k-1,   i+1, a[i],  max(M, a[i]))
                )
        return memo[index(k,i)]
    res = f(a, k-1, i=0, C=0, M=0)
    return res


def test(func):
    k = 2
    a = [10, 10, 10, 10]
    print(func(a, k), 20, func(a, k) == 20)
    
    k = 2
    a = [10, 20, 30, 40]
    print(func(a, k), 60, func(a, k) == 60)

    k = 14
    a = [189, 107, 444, 400, 84, 270, 225, 334, 410, 433, 249, 193, 487, 312, 493, 430, 422, 208, 90, 245, 337, 234, 168, 360 ]
    sol = func(a, k)
    print(sol, 740, sol == 740)


if __name__ == '__main__':
    print("naive")
    test(naive)

    print("exponential")
    test(exponential)

    print("memoized")
    test(memoized)

