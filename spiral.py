from typing import List


def spiral_order(A: List[List[int]]) -> List[int]:
    """Given a matrix of integers, return the matrix elements in spiral order.
    """
    row = 0
    col = 0
    result = []
    ROWS = len(A)
    COLS = len(A[0])
    done = [False] * COLS * ROWS
    direction = 0
    expected_len =  ROWS * COLS
    while (len(result) < expected_len):
        # right
        if direction == 0:
            while col < COLS and not done[row*COLS + col]:
                result.append(A[row][col])
                done[row*COLS + col] = True
                col += 1 
            col += -1
            row += 1
        # down
        elif direction == 1:
            while row < ROWS and not done[row*COLS + col]:
                result.append(A[row][col])
                done[row*COLS + col] = True
                row += 1
            row += -1
            col += -1
        # left
        elif direction == 2:
            while col >= 0 and not done[row*COLS + col]:
                result.append(A[row][col])
                done[row*COLS + col] = True
                col += -1
            col += 1
            row += -1
        # up
        elif direction == 3:
            while row > 0 and not done[row*COLS + col]:
                result.append(A[row][col])
                done[row*COLS + col] = True
                row += -1
            row += 1
            col += 1
        direction = (direction + 1) % 4
            
    return result


if __name__ == '__main__':
    A = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    sol = spiral_order(A)
    print()
    print(sol)
    print(sol == [1,2,3,6,9,8,7,4,5])
    print()

    A = [
        [ 1,   2,  3, 4 ],
        [ 10, 11, 12, 5 ],
        [ 9,   8,  7, 6 ]
    ]
    sol = spiral_order(A)
    print()
    print(sol)
    print(sol == [1,2,3,4,5,6,7,8,9,10,11,12])
    print()

    A = [
        [ 1,   2,  3, 4 ],
        [ 12, 13, 14, 5 ],
        [ 11, 16, 15, 6 ],
        [ 10,  9,  8, 7 ],
    ]
    sol = spiral_order(A)
    print()
    print(sol)
    print(sol == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])