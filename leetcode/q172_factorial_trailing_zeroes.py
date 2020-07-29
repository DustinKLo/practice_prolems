import math

class Solution(object):
    def trailingZeroes(self, n):
        r = 0
        v = n
        while v > 0:
            v /= 5
            r += v
        print(n, "ans", r)
        print("########################\n")
        return r

    def trailingZeroesSlow(self, n):
        """
        :type n: int
        :rtype: int
        """
        fact = math.factorial(n)
        
        trailing_zeroes = 0
        while fact % 10 == 0:
            tens = 10
            digits = 1
            while fact % tens == 0:
                if fact % 10 == 0:
                    trailing_zeroes += digits  # could also so math.log10(tens)
                    fact = fact / tens
                tens = tens * 10
                digits += 1
        print(n, "ans", trailing_zeroes)
        print("########################\n")
        return trailing_zeroes


if __name__ == '__main__':
    s = Solution()
    s.trailingZeroes(20)  # 4
    s.trailingZeroesSlow(20)  # 4
    s.trailingZeroes(25)  # 4
    s.trailingZeroesSlow(25)  # 4
    s.trailingZeroes(30)  # 4
    s.trailingZeroesSlow(30)  # 4
    s.trailingZeroes(50)  # 4
    s.trailingZeroesSlow(50)  # 4
    s.trailingZeroes(100)  # 4
    s.trailingZeroesSlow(100)  # 4
    s.trailingZeroes(150)  # 4
    s.trailingZeroesSlow(150)  # 4
    s.trailingZeroes(7221)  # 1802
    s.trailingZeroesSlow(7221)  # 1802
    s.trailingZeroes(1808548329)
