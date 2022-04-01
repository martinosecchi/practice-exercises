"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2.

Input: n = 1
Output: [["Q"]]
"""

def solve_n_queens(n: int) -> list:
    """Representation of the solution as coordinates in 2D space:
    E.g. [".Q..","...Q","Q...","..Q."] -> [(0,1), (1, 4), (2, 0), (3, 2)]

    Complexity:
        Time: O(n^3n)
        Space: O(n^2)  (n elements passed down an n-deep stack call in `search`)
    """
    
    def is_valid_pos(x: int, y: int, queens: set) -> bool:
        if (x, y) in queens: return False
        # check row
        for j in range(n):
            if (x, j) in queens: return False
        # check column
        for i in range(n):
            if (i, y) in queens: return False
        # check diagonal 1
        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            if (i, j) in queens: return False
            i, j = i - 1, j - 1
        i, j = x + 1, y + 1
        while i < n and j < n:
            if (i, j) in queens: return False
            i, j = i + 1, j + 1
        # check diagonal 2
        i, j = x - 1, y + 1
        while i >= 0 and j < n:
            if (i, j) in queens: return False
            i, j = i - 1, j + 1
        i, j = x + 1, y - 1
        while i < n and j >= 0:
            if (i, j) in queens: return False
            i, j = i + 1, j - 1
        return True


    def get_available_positions(queens: set):
        candidates = []
        for i in range(n):
            for j in range(n):
                if is_valid_pos(i, j, queens):
                    candidates.append((i, j))
        return candidates


    def search(current_queens: set = None) -> list:
        current_queens = current_queens or set()

        if len(current_queens) == n:
            return [current_queens]
        
        solutions = []
        for candidate in get_available_positions(current_queens):
            sub_solutions = search({candidate, *current_queens})
            solutions = [*solutions, *[ss for ss in sub_solutions if ss not in solutions]]
        return solutions


    def format_solutions(solutions: list):
        formatted_solutions = []
        for solution in solutions:
            formatted_solution = []
            for i in range(n):
                row = ""
                for j in range(n):
                    row += "Q" if (i, j) in solution else "."

                formatted_solution.append(row)
            formatted_solutions.append(formatted_solution)
        return formatted_solutions


    solutions = search()
    return format_solutions(solutions)



def solve_n_queens_simple(n: int) -> list:
    """Representation of the solution as 1D coordinates representing the position of the queen for each row 
    (since we know there is only one queen per row):
    E.g. [".Q..","...Q","Q...","..Q."] -> [1, 3, 0, 2]

    Complexity:
        Time: O(n^n)
        Space: O(n^2)
    """

    def get_available_positions(queens: list) -> list:
        current_queen = len(queens)
        candidates = set(range(n))
        # discard some positions
        if current_queen > 0:
            for row, col in enumerate(queens):
                candidates.discard(col)
                # discard diagonals
                dist = current_queen - row
                candidates.discard(col + dist)
                candidates.discard(col - dist)
                
        return sorted(list(candidates))             


    def search(current_queens: list = None) -> list:
        current_queens = current_queens or list()

        if len(current_queens) == n:
            return [current_queens]
        
        solutions = []
        for candidate in get_available_positions(current_queens):
            sub_solutions = search([*current_queens, candidate])
            solutions = [*solutions, *sub_solutions]
        return solutions


    def format_solutions(solutions: list):
        formatted_solutions = []
        for solution in solutions:
            current_formatted_solution = []
            for j in solution:
                row = "." * j + "Q" + "." * (n - j - 1)
                current_formatted_solution.append(row)
            formatted_solutions.append(current_formatted_solution)
        return formatted_solutions


    solutions = search()
    return format_solutions(solutions)




# n_queens_1 = solve_n_queens(1)
# assert n_queens_1 == [["Q"]], n_queens_1

# n_queens_4 = solve_n_queens(4)
# assert n_queens_4 == [
#     [".Q..","...Q","Q...","..Q."],
#     ["..Q.","Q...","...Q",".Q.."],
# ], (len(n_queens_4), n_queens_4)




n_queens_1 = solve_n_queens_simple(1)
assert n_queens_1 == [["Q"]], n_queens_1

n_queens_4 = solve_n_queens_simple(4)
assert n_queens_4 == [
    [".Q..","...Q","Q...","..Q."],
    ["..Q.","Q...","...Q",".Q.."],
], (len(n_queens_4), n_queens_4)