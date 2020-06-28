class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction_mapper = {
            "right": "down",
            "down": "left",
            "left": "up",
            "up": "right"
        }


if __name__ == '__main__':
	s = Solution()
	matrix = [
		  [1, 2, 3, 4],
		  [5, 6, 7, 8],
		  [9,10,11,12]
	]
	s.spiralOrder(matrix)
