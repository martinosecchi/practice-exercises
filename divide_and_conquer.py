"""
Exercises from the Algorithm Design book - Divide and Conquer chapter
"""

import math
from typing import List


def exercise1(arr):
	"""The given array is 'unimodal': values increase until an index p, then decrease.
	Find p.
	"""
	n = len(arr)

	def divide_and_conquer(start: int, end: int) -> int:
		if start == end:
			return start

		middle = start + math.floor((end - start) / 2.)
		if arr[middle] > arr[start]:
			return divide_and_conquer(middle, end)
		else:
			return divide_and_conquer(start, middle)

	return divide_and_conquer(0, n)


# print(exercise1([1, 2, 3, 4, 5, 4, 3]), 4)
# print(exercise1([5, 4, 3, 2, 1]), 0)
# print(exercise1([1, 2, 3, 4, 5]), 4)
# print(exercise1([10, 12, 5, 1]), 1)


def exercise2(prices):
	"""Given a list of stock prices for each day, find a way to compute when to buy and when to sell (after you buy) for maximum profit.
	In other words find i and j, i < j, so that prices[j] - prices[i] is maximized.
	"""
	n = len(prices)

	# O(n^2)
	def brute_force():
		best = 0
		besti, bestj = 0, 0
		
		for i in range(n):
			for j in range(i, n):
				profit = prices[j] - prices[i]
				if profit > best:
					best = profit
					besti, bestj = i, j

		return besti, bestj, best

	# helpers
	def index_at_min(arr, start, end):
		min_value = arr[start]
		min_pos = start
		for i in range(start, end):
			if arr[i] < min_value:
				min_value = arr[i]
				min_pos = i

		return min_pos

	def index_at_max(arr, start, end):
		max_value = arr[start]
		max_pos = start
		for i in range(start, end):
			if arr[i] > max_value:
				max_value = arr[i]
				max_pos = i

		return max_pos


	# O(n log n)
	# Recurrence relation is T(n) = 2 * T(n/2) + O(n)
	# same complexity as mergesort which is O(n log n)
	def divide_and_conquer(start: int, end: int):
		# solve optimal in first half, solve optimal in second half, check if optimal could be between the two halves

		if end - start <= 1:
			return start, end, prices[end] - prices[start]

		middle = start + math.floor((end - start) / 2.)
		i1, j1, opt1 = divide_and_conquer(start, middle)
		i2, j2, opt2 = divide_and_conquer(middle, end)

		i3 = index_at_min(prices, start, middle)
		j3 = index_at_max(prices, middle, end)
		opt3 = prices[j3] - prices[i3]


		if opt1 >= opt2 and opt1 >= opt3:
			return i1, j1, opt1
		elif opt2 >= opt1 and opt2 >= opt3:
			return i2, j2, opt2
		else:
			return i3, j3, opt3

	# O(n) 
	def dynamic_programming():
		memo = dict()

		def profit(j: int):
			"""The profit by selling on day j.
			Xj = Xj-1 + p(j) - p(j-1) 	if I have the stock.
			Xj = 0 						if I don't have the stock.
			"""
			if j not in memo:
				memo[j] = max(0, profit(j-1) + prices[j] - prices[j-1])

			return memo[j]

		def profit_with_i(i: int, j: int):
			if j not in memo:
				_, _, prev = profit_with_i(i, j-1)
				memo[j] = max(0, prev + prices[j] - prices[j-1])
				if memo[j] == 0:
					i = j

			return i, j, memo[j]


		memo[0] = 0
		# best = max(profit(j) for j in range(1, n))
		# j is argmax
		# i is min(prices[:j])
		besti, bestj, best, i = 0, 0, 0, 0
		for j in range(1, n):
			i, j, p = profit_with_i(i, j)
			if p > best:
				besti, bestj, best = i, j, p

		return besti, bestj, best


	brute = brute_force()
	dnq = divide_and_conquer(0, n-1)
	dp = dynamic_programming()
	return brute, dnq, dp

# print(exercise2([4, 3, 2, 5, 1000, 1, 10]), (2, 4, 998))
# print(exercise2([5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]), (4, 8, 4))
# print(exercise2([50, 42, 49, 20, 10, 32, 20, 14, 45, 40, 43, 42, 1]), (4, 8, 35))
# print(exercise2([9, 1, 5]), (1, 2, 4))
# print(exercise2([0, 10, 5]), (0, 1, 10))
# print(exercise2([100, 110, 0, 100, 5]), (2, 3, 100))
# print(exercise2([100, 98, 100, 110, 96, 99, 100]), (1, 3, 12))


def mergesort(arr) -> List[int]:
	
	n = len(arr)

	def mergesort_inner(start: int, end: int) -> List[int]:
		# only one element
		if start >= end:
			return [arr[start]]

		# two elements
		if end - start == 1:
			if arr[start] < arr[end]:
				return [arr[start], arr[end]]
			else:
				return [arr[end], arr[start]]

		# more elements: sort two halves, then merge
		middle = start + math.floor((end-start) / 2)
		first = mergesort_inner(start, middle)
		second = mergesort_inner(middle+1, end)

		# merge the two sorted halves together
		merged = []
		i = 0
		j = 0
		n_first = len(first) 
		n_second = len(second)
		while i < n_first or j < n_second:
			if j >= n_second or i < n_first and first[i] <= second[j]:
				merged.append(first[i])
				i += 1
			else:
				merged.append(second[j])
				j += 1

		return merged


	return mergesort_inner(0, n-1)

def mergesort_inplace(arr: List[int]) -> List[int]:

	n = len(arr)

	def swap(i: int, j: int):
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp

	def mergesort_inner(start: int, end: int):
		# one or two elements
		if end - start <= 1:
			if arr[end] < arr[start]:
				swap(start, end)
			return 

		# more elements: sort two halves, then merge
		middle = start + math.floor((end-start) / 2)
		mergesort_inner(start, middle)
		mergesort_inner(middle+1, end)

		# merge the two sorted halves
		i = start
		j = middle + 1
		while i <= middle and j <= end:
			if arr[i] <= arr[j]:
				i += 1
			else:
				# swap arr[j] with all elements until it comes at i position
				current = j
				while current > i:
					swap(current, current - 1)
					current -= 1
				i += 1
				middle += 1
				j += 1

		return 

	mergesort_inner(0, n-1)
	return arr


# print("mergesort")
# print(mergesort([6,5,4,3,2,1]))
# print(mergesort([5,3,1,4,2,6]))
# print("mergesort inplace")
# print(mergesort_inplace([6,5,4,3,2,1]))
# print(mergesort_inplace([5,3,1,4,2,6]))

