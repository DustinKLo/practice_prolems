def climbStairs(n):
	memo = [0] * (n + 1)
	def traverse(m):
		print(memo)
		if m == 0:
			return 1
		elif m < 0:
			return 0
		if memo[m] > 0:
			return memo[m]
		
		memo[m] = traverse(m - 1) + traverse(m - 2)
		return memo[m]
	
	if n < 0:
		return 0
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return traverse(n)


if __name__ == '__main__':
	print(climbStairs(35))
