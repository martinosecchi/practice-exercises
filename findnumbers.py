
# O(n)
def find_unique_numbers(arr: list):
    """
    You are given an array A containing 2*N+2 positive numbers, out of which N numbers are repeated exactly once
    and the other two numbers occur exactly once and are distinct. 
    You need to find the other two numbers and print them in ascending order.
    """
    visited = set()
    for n in arr:
        if n not in visited:
            visited.add(n)
        else:
            visited.remove(n)
    return tuple(visited)


def test():
    A = [1, 2, 3, 2, 1, 4]
    print(find_unique_numbers(A), (3,4), find_unique_numbers(A)==(3,4))

    A = [2, 1, 3, 2]
    print(find_unique_numbers(A), (1,3), find_unique_numbers(A)==(1,3))


if __name__ == '__main__':
    test()
