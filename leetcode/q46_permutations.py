class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def traverse(arr, res):
        	if len(arr) == 0:
        		ans.append(res)
        		print(res)
        		return
        	
        	for i in range(0, len(arr)):
        		# new_arr = arr[:i] + arr[i+1:]  # remove ith index from array
        		# new_res = res + [arr[i]]  # add to the result array
        		# traverse(new_arr, new_res)
        		traverse(arr[:i] + arr[i+1:], res + [arr[i]])

        traverse(nums, [])
        return ans


if __name__ == '__main__':
	s = Solution()
	s.permute([1,2,3])
	print("#########################\n")
	s.permute([1])
	print("#########################\n")
	s.permute(list(range(5)))
	print("#########################\n")
