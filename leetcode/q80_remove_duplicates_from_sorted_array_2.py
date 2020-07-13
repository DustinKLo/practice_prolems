class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        
        if len(nums) < 3:
            return nums

        i = 0  # starting pointer
        j = 2  # end pointer

        # loop i and j until they match
        # inner loop will pop value from nums until ith and jth letter dont match no more
        while i < len(nums):
            if j < len(nums):
                if nums[i] == nums[j]:
                    # inner while loop
                    while j < len(nums) and nums[i] == nums[j]:
                        nums.pop(j)
                j += 1
            i += 1
        print(nums)
        print("ans: %d" % i)
        print("########################################\n")
        return i


if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates([1,1,1,2,2,3])
    s.removeDuplicates([0,0,1,1,1,1,2,3,3])
    s.removeDuplicates([1,1,1])
