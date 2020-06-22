class Solution(object):
	@staticmethod
	def print_board(board):
		for row in board:
			print(row)

	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		self.print_board(board)

		'check horizontals'
		for row in board:
			row = filter(lambda x: x != '.', row)
			if len(set(row)) != len(row):
				print("INVALID rows")
				return False
		print("valid rows")

		'check verticals'
		for i in range(9):  # columns
			column = []
			for j in range(9):  # rows
				ch = board[j][i]
				column.append(ch) if ch != '.' else None
			if len(column) != len(set(column)):
				print("INVALID columns")
				return False
		print("valid columns")


		'check grids'
		y = 0
		while y < 9:
			x = 0
			while x < 9:
				grid = []
				grid += board[y][x:x+3] + board[y+1][x:x+3] + board[y+2][x:x+3]
				grid = filter(lambda x: x != '.', grid)
				if len(set(grid)) != len(grid):
					print("INVALID grids")
					return False
				x += 3
			y += 3
		print("valid grids")
		print("sudoku IS valid")
		return True


if __name__ == '__main__':
	s = Solution()

	brd = [
		["5","3",".",".","7",".",".",".","."],
		["6",".",".","1","9","5",".",".","."],
		[".","9","8",".",".",".",".","6","."],
		["8",".",".",".","6",".",".",".","3"],
		["4",".",".","8",".","3",".",".","1"],
		["7",".",".",".","2",".",".",".","6"],
		[".","6",".",".",".",".","2","8","."],
		[".",".",".","4","1","9",".",".","5"],
		[".",".",".",".","8",".",".","7","9"]
	]
	s.isValidSudoku(brd)