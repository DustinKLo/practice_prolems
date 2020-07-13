class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        
        nums_len = len(nums)
        if nums_len < 3:
            return nums_len

        i = 0  # starting pointer
        j = 2  # end pointer

        # loop i and j until they match
        # inner loop will pop value from nums until ith and jth letter dont match no more
        while j < nums_len:
            if nums[i] == nums[j]:
                # inner while loop
                while j < nums_len and nums[i] == nums[j]:
                    nums.pop(j)
                    nums_len -= 1  # decreasing to keep length of array consistent
            j += 1
            i += 1
        print(nums)
        print("ans: %d" % i)
        print("########################################\n")
        return nums_len


if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates([1,1,1,2,2,3])
    s.removeDuplicates([0,0,1,1,1,1,2,3,3])
    s.removeDuplicates([1,1,1])
