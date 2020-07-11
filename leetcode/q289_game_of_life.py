class Solution(object):
	@staticmethod
	def print_board(brd):
		for row in brd:
			print(row)

	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: None Do not return anything, modify board in-place instead.
		"""
		def check_board(y, x):
			if y < 0 or y > len(board) - 1:
				return 0
			if x < 0 or x > len(board[y]) - 1:
				return 0

			return board[y][x]

		self.print_board(board)
		print("")
		
		# keep coordinate of those alive and those dead
		new_dead = set()
		new_alive = set()
		
		for j in range(len(board)):  # rows
			for i in range(len(board[j])):  # columns
				live_cells = check_board(j + 1, i - 1) + check_board(j + 1, i) + check_board(j + 1, i + 1) + \
							 check_board(j, i - 1) + check_board(j, i + 1) + \
							 check_board(j - 1, i - 1) + check_board(j - 1, i) + check_board(j - 1, i + 1)
				if board[j][i] == 1:
					if live_cells < 2:
						new_dead.add((j, i))
					elif live_cells > 3:
						new_dead.add((j, i))
				else:
					if live_cells == 3:
						new_alive.add((j, i))
		
		# replace board with coordinates in new_alive and new_dead
		for _y, _x in new_dead:
			board[_y][_x] = 0

		for _y, _x in new_alive:
			board[_y][_x] = 1
		self.print_board(board)


if __name__ == '__main__':
	s = Solution()
	matrix = [
	  [0,1,0],
	  [0,0,1],
	  [1,1,1],
	  [0,0,0]
	]
	s.gameOfLife(matrix)
