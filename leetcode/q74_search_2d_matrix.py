class Solution(object):
    @staticmethod
    def binary_search(arr, target):
        def traverse(target, left, right):
            if left > right:
                return -1
            
            mid = int((left + right) / 2)
            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                return 0 + traverse(target, mid + 1, right)
            else:
                return 0 + traverse(target, left, mid - 1)
        
        idx = traverse(target, 0, len(arr) - 1)
        return idx

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # go through each row and check if target is between the min and max
        target_row = []
        for row in matrix:
        	if len(row) == 0:
        		return False
            if target >= row[0] and target <= row[-1]:
                target_row = row
                break

        # if found, extract the array from the matrix
        #     perform binary search on that particular array for the target
        if target_row == []:
            return False

        idx = self.binary_search(target_row, target)
        return False if idx == -1 else True

if __name__ == '__main__':
    s = Solution()

    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    s.searchMatrix(matrix, 3)
    s.searchMatrix(matrix, 13)
    s.searchMatrix(matrix, 100)
