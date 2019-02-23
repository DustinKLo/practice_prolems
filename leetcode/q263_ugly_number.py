class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        
        primes = [2, 3, 5]
        for p in primes:
            # print("currently at prime ", p)
            while num % p == 0:
                num = num / p
                # print(num, p)
                if num == 1:
                    return True
