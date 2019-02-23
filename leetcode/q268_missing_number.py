class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(0, len(nums)):
            if i != nums[i]:
                return i
        return i + 1
