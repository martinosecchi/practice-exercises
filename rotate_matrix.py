from typing import List
import math


def index(i: int, j: int, N: int) -> int:
    """Given two indexes i and j of a 2D array of size NxN, this function returns a single index 
    of where to find the same element in a 1D representation of the same 2D array
    """
    return i*N + j


def rotate_matrix(M: List[int]):
    """Rotates a flattened matrix M of size NxN by 90 degrees counterclockwise and in-place
    """  
    N = int(math.sqrt(len(M)))
    for x in range(0, int(N/2)):
        for y in range(x, N-x-1):
            temp = M[index(x, y, N)]
            M[index(x, y, N)] = M[index(y, N-1-x, N)]
            M[index(y, N-1-x, N)] = M[index(N-1-x, N-1-y, N)]
            M[index(N-1-x, N-1-y, N)] = M[index(N-1-y, x, N)]
            M[index(N-1-y, x, N)] = temp
    return M


def print_sq_mx(M: List[int]):
    """Prints a square flattened matrix M of size NxN
    """
    N = int(math.sqrt(len(M)))
    print()
    for i in range(N):
        for j in range(N):
            print(M[index(i, j, N)], end='')
        print()
    print()


if __name__ == '__main__':
    M = list(map(int, "1 2 3 4 5 6 7 8 9".split()))
    print(rotate_matrix(M) == [3, 6, 9, 2, 5, 8, 1, 4, 7])
    # [1, 2, 3],      [3, 6, 9],
    # [4, 5, 6],  ->  [2, 5, 8],
    # [7, 8, 9],      [1, 4, 7],
    #
    # 0,0     2,0
    # 0,1     1,0
    # 0,2     0,0
    # 1,0     2,1
    # 1,1     1,1
    # 1,2     0,1
    # 2,0     2,2
    # 2,1     1,2
    # 2,2     0,2

    N = 5
    M = "76 59 82 17 70 42 1 83 39 56 66 28 65 29 53 88 82 45 38 51 89 24 5 51 75".split()
    print(rotate_matrix(M) == "70 56 53 51 75 17 39 29 38 51 82 83 65 45 5 59 1 28 82 24 76 42 66 88 89".split())

