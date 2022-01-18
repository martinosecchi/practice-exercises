

def parenthesis(n: int):
	"""Returns a list of all possible combinations of parenthesis with n pairs.
	The combinations must be valid (each open parenthesis is also closed)
	"""
	solutions = set()

	def inner(to_open: int, to_close: int, current: str):
		# reached the end of this branch of possible solutions
		if to_open == 0 and to_close == 0:
			solutions.add(current)
			return

		if to_open > 0:
			inner(to_open - 1, to_close, current +  "(")

		if to_close > 0 and to_close > to_open:
			inner(to_open, to_close - 1, current + ")")

	inner(n, n, "")
	return list(solutions)

if __name__ == '__main__':
	solutions = parenthesis(3)
	print(solutions)