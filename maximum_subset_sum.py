"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset. 
It is possible that the maximum sum is 0, the case when all elements are negative.

Example
arr = [-2, 1, 3, -4, 5]
The following subsets with more than 1 element exist. These exclude the empty subset and single element subsets which are also valid.

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8
The maximum subset sum is 8. Note that any individual element is a subset as well.
"""

def recursive_max_subset_sum(arr):
    
    n = len(arr)
    memo = dict()
    
    def find_subset_sums(i, current_sum):

        if i in memo and memo[i] >= current_sum:
            return memo[i]

        if i >= n - 2:
            memo[i] = current_sum
            return current_sum
        
        local_max = current_sum
        for j in range(i + 2, n):
            branch_sum = find_subset_sums(j, current_sum + arr[j])
            local_max = max(branch_sum, local_max)
        
        memo[i] = local_max
        return local_max
        

    res = find_subset_sums(-2, 0)
    return res


def max_subset_sum(arr):
    n = len(arr)
    best_sums = [0] * n
    best_so_far = 0
    for i in range(n):
        num = arr[i]
        best_sums[i] = max(best_sums[i], num, best_so_far)
        if i >= 2:
            best_sums[i] = max(best_sums[i], best_sums[i-2] + num)
        best_so_far = best_sums[i]

    return best_so_far
    

if __name__ == '__main__':

    examples = [
        ([3, 7, 4, 6, 5], 13),
        ([-1, -2, -3], 0),
        ([2, 1, 5, 8, 4], 11),
        ([3, 5, -7, 8, 10], 15),
    ]

    print("recursive:")
    for inputs, result in examples:
        try:
            res = recursive_max_subset_sum(inputs)
            print(f"expected: {result}, result: {res}, match: {result == res}")
        except RecursionError:
            print("recursion error")

    print("linear:")
    for inputs, result in examples:
        res = max_subset_sum(inputs)
        print(f"expected: {result}, result: {res}, match: {result == res}")

    
