class GenerateParanthesis:
	def __init__(self):
		self.patterns = list()

	def traverse(self, pattern, target, num_left, num_right):
		if num_left + num_right > target:
			return

		if num_right > num_left:
			return

		if num_left + num_right == target:
			if num_left == num_right:
				self.patterns.append(pattern)
			return

		self.traverse(pattern + '(', target, num_left + 1, num_right)
		self.traverse(pattern + ')', target, num_left, num_right + 1)

	def generate_paranthesis(self, num):
		self.patterns = []
		if num % 2 != 0:
			print('Odd number of paranthesis!!!')

		self.traverse(pattern='', target=num, num_left=0, num_right=0)
		counter = 1
		print('number of paranthesis: %i' % num)
		for x in self.patterns:
			print('%i: %s' % (counter, x))
			counter += 1
		print('')


if __name__ == '__main__':
	test_case = GenerateParanthesis()
	test_case.generate_paranthesis(2)
	test_case.generate_paranthesis(4)
	test_case.generate_paranthesis(6)
	test_case.generate_paranthesis(8)
	test_case.generate_paranthesis(10)
