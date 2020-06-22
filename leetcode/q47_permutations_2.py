class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()

        def traverse(arr, res):
        	if len(arr) == 0:
        		ans.add(res)  # res is a tuple
        		return
        	
        	for i in range(0, len(arr)):
        		traverse(arr[:i] + arr[i+1:], res + (arr[i],))

        # empty tuple because you can create a unique set of tuples
        traverse(nums, ())
        for i in ans:
            print(i)
        return ans


if __name__ == '__main__':
	s = Solution()
	s.permuteUnique([1,2,3])
	print("#########################\n")
	s.permuteUnique([1])
	print("#########################\n")
	s.permuteUnique([1,1,2])
	print("#########################\n")
