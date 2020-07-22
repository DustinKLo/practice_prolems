import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        nums = [0] * (n + 1)
        for i in range(2, int(math.sqrt(n + 1)) + 1):
            for j in range(2, int(n / i + 1)):
                nums[i * j] = 1

        num_primes = 0
        for i in range(2, len(nums) - 1):
            if nums[i] == 0:
                num_primes += 1
                print(i)
        
        print("########################################")
        return num_primes


if __name__ == '__main__':
    s = Solution()
    s.countPrimes(10)
    s.countPrimes(5)
    s.countPrimes(100)
