class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        print(n)
        if n <= 0:
            return False
        if n <= 2:
            return True
        if n % 2 != 0:
            return False

        divisor = 2
        while n > 0:
            n = n / divisor
            # divisor *= 2
            print(n, divisor)

            if n % 2 != 0:
                return False

            if divisor >= n:
                divisor = 2

            if n == 2:
                return True
        return False



if __name__ == '__main__':
    print(Solution().isPowerOfTwo(4728732979278742389732))
    print("")
    print(Solution().isPowerOfTwo(10000000000))
    print("")
    print(Solution().isPowerOfTwo(1048576))
    print("")
    print(Solution().isPowerOfTwo(20))
    print("")
    print(Solution().isPowerOfTwo(33554432))
    print("")
    print(Solution().isPowerOfTwo(1125899906842624))
