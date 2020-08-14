class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        target = len(nums) // 3
        counts = {}
        ans = []
        
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
        
        for k, v in counts.items():
            if v > target:
                ans.append(k)

        return ans
