class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = []
        for val in nums:
            if val not in cache:
                cache.append(val)
            else:
                cache.remove(val)
            
        print(cache)
        return cache[0]
        