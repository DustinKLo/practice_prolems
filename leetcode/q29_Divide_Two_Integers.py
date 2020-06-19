class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        print(dividend, divisor)

        sign = 1
        if dividend < 0:
        	sign *= -1
        	dividend *= -1
        if divisor < 0:
        	sign *= -1
        	divisor *= -1

        if divisor == 0:
        	return 0
        if divisor == 1:
        	if sign * dividend > INT_MAX:
	        	dividend = INT_MAX
	        if sign * dividend < INT_MIN:
	        	dividend = INT_MIN
        	return sign * dividend
        if dividend == divisor:
        	return sign * 1

        ans = 0
        n = 1
        while dividend >= divisor:
            while dividend >= divisor:
                if dividend - divisor ** n < 0:
                    break
                dividend = dividend - divisor ** n
                ans = ans + (divisor ** (n - 1))
                print(ans, n, dividend)
                n += 1
            n = 1
        print(sign * ans)
        return sign * ans


if __name__ == '__main__':
    s = Solution()
    
    s.divide(40, 3)
    print("######################\n")
    s.divide(3000, 3)
    print("######################\n")
    s.divide(48290841, 3)
    print("########################\n")
    s.divide(48290841, 1)
    print("########################\n")
    s.divide(48290841, -1)
    print("########################\n")
    s.divide(7, -3)
    print("########################\n")
    s.divide(-2147483648, -1)
    print("########################\n")
    s.divide(-2147483648, 1)
    print("########################\n")
    s.divide(-2147483648, 2)
    print("########################\n")
    s.divide(2147483648, 2)
    print("########################\n")
    s.divide(100000, 3)
