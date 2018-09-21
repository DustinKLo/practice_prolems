
# regular fibonacci, not cached
# very slow when going past 40
def fib(n):
	if n <= 1:
		return 1
	return fib(n - 1) + fib(n - 2)


# cached fibonacci, extremely fast
def fib_memoized(n):
	cache = { 1: 1, 2: 1 }

	def fib(n): 
		if n < 0:
			return 0
		if n <= 2:
			return 1

		if cache.get(n):
			return cache[n]

		# the previous values (n-2) or (n-1) is cached then grab it from the cache dictionary
		# or else calculate it with recursion
		if cache.get(n-1):
			val1 = cache[n-1]
		else:
			val1 = fib(n-1)

		if cache.get(n-2):
			val2 = cache[n-2]
		else:
			val2 = fib(n-2)

		# caching the value so that we can retrieve it quickly after
		cache[n] = val1 + val2
		return val1 + val2

	for i in range(1, n+1):
		print('{}: {}'.format(i, fib(i)))
	
	return fib(n)


if __name__ == '__main__':
	i = 1000
	f = fib_memoized(i)
	print('Fibonacci number for {} is {}'.format(i, f))
