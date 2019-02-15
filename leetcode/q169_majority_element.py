class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        for x in nums:
            if x not in cache:
                cache[x] = 1
            else:
                cache[x] += 1
        
        # print(cache)
        max_key = max(cache, key=cache.get)
        max_value = cache[max_key]
        # print(max_key, max_value)
        return max_key
        