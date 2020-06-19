class Solution(object):
	def __init__(self):
		self.ans = []

	def traverse(self, cand, value, ans):
		for i in range(0, len(cand)):
			c = cand[i]
			if c == 0:
				return

			diff = value - c
			
			if diff < 0:
				return

			if diff == 0:
				if ans + [c] not in self.ans:
					print(ans + [c])
					self.ans.append(ans + [c])
				return

			new_arr = cand[:i] + cand[i+1:]
			self.traverse(new_arr[i:], diff, ans + [c])


	def combinationSum2(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		candidates.sort()

		self.ans = []
		self.traverse(candidates, target, [])
		return self.ans


if __name__ == '__main__':
	s = Solution()
	s.combinationSum2([2,3,6,7], 7)
	print("#########################\n")
	s.combinationSum2([2,3,5], 8)
	print("#########################\n")
	s.combinationSum2([8,7,4,3], 11)
	print("#########################\n")
	s.combinationSum2([10,1,2,7,6,1,5], 8)
	print("#########################\n")
