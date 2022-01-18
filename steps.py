"""
How many ways do you have to cross N stairs?
at every step you can either go 1 up or 2
"""

# O (2^n)
def f1(N):
    if N < 0:
        return 0
    if N == 0:
        return 1
    return f1(N-1) + f1(N-2)

# O (n)
def f2(N):
    memo = {}
    memo[-1] = 0
    memo[0] = 1
    memo[1] = 1
    def get(N):
        if not memo.get(N):
            memo[N] = get(N-1) + get(N-2)
        return memo[N]
    return get(N)
    

for f in (f1, f2):
    print()
    print(f(1), 1, f(1) == 1)
    assert f(1) == 1
    print(f(2), 2, f(2) == 2)
    assert f(2) == 2
    print(f(3), 3, f(3) == 3)
    assert f(3) == 3
    print(f(4), 5, f(4) == 5)
    assert f(4) == 5
    print(f(5), 8, f(5) == 8)
    assert f(5) == 8

#                 5
#             4       3
#         3   2       2   1
#     2   1   1,0   1,0   0
# 1,0     0   0     0
# 0

