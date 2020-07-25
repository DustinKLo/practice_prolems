class Solution(object):
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[List[int]]
		:type newInterval: List[int]
		:rtype: List[List[int]]
		"""
		i = 0
		while i < len(intervals):
			cur = intervals[i]
			if newInterval[0] <= cur[1] and newInterval[1] >= cur[0]:
				# replace current with new merged interval
				newInterval = [min(cur[0], newInterval[0]), max(cur[1], newInterval[1])]
				intervals[i] = newInterval
				intervals = intervals[:i] + intervals[i+1:]
				continue
			i += 1

		inserted = False
		for i in range(len(intervals)):
			# check if cur is greater than newInterval
			cur = intervals[i]
			if newInterval[1] < cur[0]:
				intervals = intervals[:i] + [newInterval] + intervals[i:]
				inserted = True
				break

		if len(intervals) == 0:
			return [newInterval]
		
		# check end
		if inserted is False:
			intervals += [newInterval]

		return intervals


if __name__ == '__main__':
	s = Solution()
	
	# [[1,2],[3,10],[12,16]]
	s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
	
	# [[1,5],[6,9]] 
	s.insert([[1,3],[6,9]], [2,5])

	# [[1,5],[6,8]]
	s.insert([[1,5]], [6,8])

	s.insert([], [4,5])

	s.insert([[1,5]], [2,3])
