from typing import List

Matrix = List[List[int]]

def remove_islands(matrix: Matrix) -> Matrix:
    # 0 -> white
    # 1 -> black
    # remove all "islands" of black pixels if the island is not connected to the border
    n = len(matrix)
    m = len(matrix[0]) if n else 0
    visited = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j] and not is_connected_to_border(matrix, i, j, visited):
                matrix = remove_island_at(matrix, i, j)
    return matrix
    

def is_connected_to_border(matrix: Matrix, i: int, j: int, visited: Matrix) -> bool:
    n = len(matrix)
    m = len(matrix[0]) if n else 0

    i_out_of_bound = i < 0 or i >= n
    j_out_of_bound = j < 0 or j >= m
    if i_out_of_bound or j_out_of_bound or matrix[i][j] == 0 or visited[i][j]:
        return False

    visited[i][j] = True
    is_border = i == 0 or i == n - 1 or j == 0 or j == m - 1
    # evaluate all direction to fill up `visited` 
    connected_up = is_connected_to_border(matrix, i - 1, j, visited)
    connected_down = is_connected_to_border(matrix, i + 1, j, visited)
    connected_left = is_connected_to_border(matrix, i, j - 1, visited)
    connected_right = is_connected_to_border(matrix, i, j + 1, visited)
    return (
        is_border or 
        connected_up or 
        connected_down or 
        connected_right or 
        connected_left
    )


def remove_island_at(matrix: Matrix, i: int, j: int) -> Matrix:
    n = len(matrix)
    m = len(matrix[0]) if n else 0

    i_out_of_bound = i < 0 or i >= n
    j_out_of_bound = j < 0 or j >= m
    if i_out_of_bound or j_out_of_bound or matrix[i][j] == 0:
        return matrix

    matrix[i][j] = 0
    remove_island_at(matrix, i - 1, j)
    remove_island_at(matrix, i + 1, j)
    remove_island_at(matrix, i, j - 1)
    remove_island_at(matrix, i, j + 1)
    return matrix


def pretty_format(matrix: Matrix):
    return "\n".join([str(row) for row in matrix])


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]
result = remove_islands(matrix)
expected = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
]


assert result == expected, f"Wrong result. Expected: \n{pretty_format(expected)}\nGot: \n{pretty_format(result)}"
