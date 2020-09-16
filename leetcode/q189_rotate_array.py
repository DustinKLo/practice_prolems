class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ls_len = len(nums)
        k_mod = k % ls_len
        nums_new = nums[ls_len - k_mod:] + nums[:ls_len - k_mod]
        
        for i in range(len(nums_new)):
            nums[i] = nums_new[i]
