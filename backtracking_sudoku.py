"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Constraints.

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

Example 1.

Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]
"""
from typing import List, Tuple, Union


def solve_sudoku(board: List[List[str]]) -> List[List[str]]:

    n = len(board)
    INCOMPLETE = "."
    SQUARE_SIZE = int(n / 3)

    def is_complete(current_board: List[List[str]]) -> bool:
        for row in current_board:
            if INCOMPLETE in row:
                return False
        return True

    def get_incomplete_positions(current_board: List[List[str]]) -> List[Tuple[int]]:
        return [
            (i, j) for i in range(n) for j in range(n) 
            if current_board[i][j] == INCOMPLETE
        ]

    def get_candidates_for_position(current_board: List[List[str]], pos: Tuple[int]) -> List[int]:
        x, y = pos
        candidates = set(map(str, range(1, n + 1)))

        # discard anything in same row, column and square
        for j in range(n):
            candidates.discard(current_board[x][j])

        for i in range(n):
            candidates.discard(current_board[i][y])
        
        square_start_x, square_start_y = SQUARE_SIZE * int(x / SQUARE_SIZE), SQUARE_SIZE * int(y / SQUARE_SIZE)
        for i in range(square_start_x, square_start_x + SQUARE_SIZE):
            for j in range(square_start_y, square_start_y + SQUARE_SIZE):
                candidates.discard(current_board[i][j])

        return sorted(list(candidates))

    def fill(current_board: List[List[str]]) -> Union[None, List[List[str]]]:
        if is_complete(current_board):
            return current_board

        easiest_position = None
        position_candidates = []
        for pos in get_incomplete_positions(current_board):
            candidates = get_candidates_for_position(current_board, pos)
            if easiest_position is None or len(candidates) < len(position_candidates):
                easiest_position = pos
                position_candidates = candidates

        if not position_candidates:
            return None

        for candidate in position_candidates:
            i, j = easiest_position
            current_board[i][j] = str(candidate)
            filled_board = fill(current_board)

            if filled_board is not None:
                return filled_board

            current_board[i][j] = INCOMPLETE
        return None

    return fill(board)


def pretty_string(board: Union[List[List[str]], None]) -> str:
    if board is None:
        return "None"
    string = ""
    for row in board:
        string += str(row) + "\n"

    return string


tests = [
    [
        [".","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ],    
    [
        [".","3","4","6","7","8","9",".","2"],
        ["6","7","2","1","9","5","3","4","8"],
        [".","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ],
    [ 
        [".",".",".","6","7","8","9","1","2"],
        [".",".",".","1","9","5","3","4","8"],
        [".",".",".","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ],
    [ 
        ["5",".","4","6",".","8",".","1","."],
        ["6","7","2","1","9",".","3","4","."],
        ["1","9","8","3",".","2",".","6","7"],
        ["8",".","9","7",".","1","4","2","3"],
        ["4","2","6",".","5","3","7","9","."],
        ["7","1",".","9",".","4",".","5","6"],
        ["9",".","1","5","3","7","2","8","."],
        ["2","8","7","4","1",".",".","3","5"],
        [".","4",".","2","8","6",".","7","9"]
    ],
    [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ],
]
expected = [ 
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]

for test_board in tests:
    solution = solve_sudoku(test_board)
    assert solution == expected, f"Wrong answer, \nExpected: \n{pretty_string(expected)}\nGot: \n{pretty_string(solution)}"
    print("correct")
