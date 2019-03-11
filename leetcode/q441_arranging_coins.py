class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        current_level = 0
        while n > 0:
            n = n - current_level
            # print(current_level, n)
            if n < 0:
                break
            current_level += 1
        return current_level - 1
