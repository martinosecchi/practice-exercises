"""
Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even.
We play a game against an opponent by alternating turns. In each turn,
a player selects either the first or last coin from the row, removes it from the row permanently,
and receives the value of the coin. 
Determine the maximum possible amount of money we can definitely win if we move first.

Note: The opponent is as clever as the user.

Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
Let us understand the problem with few examples:

    1. 5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)

    2. 8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)

Does choosing the best at each move give an optimal solution?

No. In the second example, this is how the game can finish:

1.
…….User chooses 8.
…….Opponent chooses 15.
…….User chooses 7.
…….Opponent chooses 3.
Total value collected by user is 15(8 + 7)

2.
…….User chooses 7.
…….Opponent chooses 8.
…….User chooses 15.
…….Opponent chooses 3.
Total value collected by user is 22(7 + 15)

F(i, j)  represents the maximum value the user can collect from 
         i'th coin to j'th coin.

    F(i, j)  = Max(Vi + min(F(i+2, j), F(i+1, j-1) ), 
                   Vj + min(F(i+1, j-1), F(i, j-2) )) 
Base Cases
    F(i, j)  = Vi           If j == i
    F(i, j)  = max(Vi, Vj)  If j == i+1
"""

def select_coin(arr):
    n = len(arr)
    memo = []
    for i in range(n):
        memo.append([])
        for j in range(n):
            memo[i].append(0)
 
    for gap in range(n):
        i = -1
        for j in range(gap, n):
            i+=1
            x = memo[i + 2][j]       if ((i + 2) <= j)        else 0
            y = memo[i + 1][j -  1]  if ((i + 1) <= (j - 1))  else 0
            z = memo[i][j - 2]       if (i <= (j - 2))        else 0
 
            memo[i][j] = max(
                            arr[i] + min(x, y),
                            arr[j] + min(y, z)
                        )
    return memo[0][n - 1]


def test():

    a = [8, 15, 3, 7]
    print(a, select_coin(a), select_coin(a) == 22)  # 22

    a = [2, 2, 2, 2]
    print(a, select_coin(a), select_coin(a) == 4)  # 4

    a = [20, 30, 2, 2, 2, 10]
    print(a, select_coin(a), select_coin(a) == 42)  # 42
    
if __name__ == '__main__':
    test()