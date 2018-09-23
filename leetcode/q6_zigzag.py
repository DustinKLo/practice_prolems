
def print_canvas(canvas):
	for row in canvas:
		if len(row) > 0:
			print(row)

def convert(s, numRows):
	"""
	:type s: str
	:type numRows: int
	:rtype: str
	"""
	canvas = ['' for i in range(numRows)]
	row = 0
	direction = -1

	word_index = 0
	for ch in s:
		if direction == -1:# write straight down
			if row == numRows - 1: 
				direction *= -1
			else:
				if numRows == 1:
					canvas[0] += ch
				else:
					canvas[row] += ch
				row += 1

		if direction == 1: # write diaganol up
			canvas[row] += ch

			if row == 0:
				direction *= -1
				row += 1
			else:
				for i in range(0, numRows):
					if canvas[i] != row:
						canvas[i] += '\t'
				row -= 1

	print_canvas(canvas)
	
	ans = ''
	for row in canvas:
		ans += row.replace('\t', '')
	return ans


if __name__ == '__main__':
	x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	rows = 4
	ans = convert(x, rows)
	print(ans)
