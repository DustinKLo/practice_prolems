import math

class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return []
        
        ans = set()
        while n > 1:
            # n is the denomenator
            numerator = 1
            while numerator < n:
                x = math.gcd(n, numerator)
                ans.add("%d/%d" % (int(numerator / x), int(n / x)))
                numerator += 1
            n -= 1
        print(ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.simplifiedFractions(4)
    s.simplifiedFractions(100)
