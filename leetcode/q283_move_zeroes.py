class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                continue
            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
                j += 1

        print(nums)

if __name__ == "__main__":
    Solution().moveZeroes([0,0,0,0] + list(range(100)))