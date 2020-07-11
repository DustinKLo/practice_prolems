class Solution:
	@staticmethod
	def print_matrix(mat):
		for row in mat:
			print(row)

	def setZeroes(self, matrix):
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		self.print_matrix(matrix)
		print("")
		
		# find all zero coordinates
		zeroes = set()  # (y, x)
		for j in range(len(matrix)):  # row
			for i in range(len(matrix[j])):  # column
				if matrix[j][i] == 0:
					zeroes.add((j, i))

		# for each zero coordinate:
		for _y, _x in zeroes:
			# zero out the corresponding row
			for i in range(len(matrix[_y])):
				matrix[_y][i] = 0

			# zero out the correspoding column
			for i in range(len(matrix)):
				matrix[i][_x] = 0

		self.print_matrix(matrix)
		print("########################\n")


if __name__ == '__main__':
	s = Solution()
	matrix = [
	  [1,1,1],
	  [1,0,1],
	  [1,1,1]
	]
	s.setZeroes(matrix)

	matrix = [
	  [0,1,2,0],
	  [3,4,5,2],
	  [1,3,1,5]
	]
	s.setZeroes(matrix)