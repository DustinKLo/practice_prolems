def z_plus_plus(string):
	if len(string) % 2 != 0:
		return False
	
	stack = []
	opening_chars = ['(', '[', '{']
	mapper = {
		')': '(',
		']': '[',
		'}': '{',
	}
	for char in string:
		if char in opening_chars:
			stack.append(char)
		else:
			if len(stack) == 0:
				return False
			if mapper[char] == stack[-1]:
				stack.pop(-1)

	if len(stack) > 0:
		return False
	else:
		return True


if __name__ == '__main__':
	x = '[]{}()'
	print(x, z_plus_plus(x))
	x = '{([])}'
	print(x, z_plus_plus(x))
	x = '()[{}]'
	print(x, z_plus_plus(x))
	x = '[{}()]'
	print(x, z_plus_plus(x))
	x = '[({)}]'
	print(x, z_plus_plus(x))
	x = '()()()()()()((()))()()(((())))(())'
	print(x, z_plus_plus(x))
