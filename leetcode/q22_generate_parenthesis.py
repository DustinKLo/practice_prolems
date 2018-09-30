
def generateParenthesis(n):
	"""
	:type n: int
	:rtype: List[str]
	"""
	ans = []
	
	def _generate(cur, left, right):
		if left < right:
			return
		
		if left == 0 and right == 0:
			ans.append(cur)
			return

		if left > 0:
			_generate(cur + ')', left - 1, right)
		if right > 0:
			_generate(cur + '(', left, right - 1)

	_generate('', n, n)
	return ans

if __name__ == '__main__':
	print(generateParenthesis(3))
	print(generateParenthesis(4))
