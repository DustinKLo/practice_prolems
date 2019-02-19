class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = 0

        while True:
            while n > 0:
                # print(n % 10, (n % 10) ** 2, ans)
                ans += (n % 10) ** 2
                n = n / 10

            if ans == 1:
                return True
            elif ans % 145 == 0:
                return False
            else:
                n = ans
                ans = 0
        return False

if __name__ == "__main__":
	solution = Solution()
	print(solution.isHappy(482390))
	print(solution.isHappy(11111111))
	print(solution.isHappy(100000))
