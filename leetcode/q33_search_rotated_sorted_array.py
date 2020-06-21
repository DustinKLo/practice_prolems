class Solution(object):
	def __init__(self):
		self.arr = []

	@staticmethod
	def find_pivot(arr):
		i = 0
		while i < len(arr) - 1:
			if arr[i] > arr[i + 1]:
				return i + 1, arr[i + 1]
			i += 1
		return 0, arr[0]

	def traverse(self, target, left, right):
		if left > right:
			return -1
		
		mid = int((left + right) / 2)
		print(left, mid, right)
		
		if self.arr[mid] == target:
			return mid

		if self.arr[mid] < target:
			return 0 + self.traverse(target, mid + 1, right)
		else:
			return 0 + self.traverse(target, left, mid - 1)

	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		print(nums, target)
		if len(nums) == 0:
			return -1
		self.arr = nums

		pivot_idx = 0
		pivot_idx, pivot_val = self.find_pivot(nums)
		print("pivot_idx", pivot_idx, "pivot_val", pivot_val)
		if pivot_val == target:
			return pivot_idx
		
		if pivot_idx == 0:
			right = len(nums) - 1
			idx = self.traverse(target, pivot_idx, right)
		elif nums[0] > target:
			# target on right side of pivot
			print("nums[0] > target")
			right = len(nums) - 1
			idx = self.traverse(target, pivot_idx, right)
		else:
			print("else")
			# target on left side of pivot
			idx = self.traverse(target, 0, pivot_idx)
		print(idx)
		return idx


if __name__ == '__main__':
	s = Solution()

	idx = s.search([4,5,6,7,0,1,2], 0)
	print("#############\n")
	idx = s.search([4,5,6,7,0,1,2], 3)
	print("#############\n")
	idx = s.search([0,1,2,3,4,5,6,7], 3)
	print("#############\n")
	idx = s.search([1,2,3,4,5,6,7,0], 3)
	print("#############\n")
	idx = s.search([16,17,18,19,20,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 3)
	print("#############\n")
	idx = s.search([1,3], 3)
	print("#############\n")
	idx = s.search([3,1], 3)
	print("#############\n")
