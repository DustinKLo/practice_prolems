class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        og = num
        if num >= 4000:
        	return ""

        # reduce thousands
        while num >= 1000:
        	div = num / 1000
        	num = num % 1000
        	ans = ans + "M" * div
        
        # check 500s
        if num >= 900:
        	ans = ans + "CM"
        	num = num - 900
        if num >= 500:
        	ans = ans + "D"
        	num = num - 500
        	if num >= 100:
        		ans = ans + "C"
        		num = num - 100
        if num >= 400:
        	ans = ans + "CD"
        	num = num - 400

        if num >= 100:
        	ans = ans + "C" * (num / 100)
        	num = num - 100 * (num / 100)

        # reduce hundreds
        if num >= 90:
        	ans = ans + "XC"
        	num = num - 90
        if num >= 50:
        	ans = ans + "L"
        	num = num - 50
        	ans = ans + "X" * (num / 10)
        	num = num - 10 * (num / 10)
        if num >= 40:
        	ans = ans + "XL"
        	num = num - 40
        elif num >= 20:
        	ans = ans + "X" * (num / 10)
        	num = num - 10 * (num / 10)

        if num >= 10:
        	ans = ans + "X"
        	num = num - 10
        # redice 10s
        if num >= 9:
        	ans = ans + "IX"
        	num = num - 9

        if num >= 5:
        	ans = ans + "V"
        	num = num - 5
        	ans = ans + "I" * (num / 1)
        	num = num - 1 * (num / 1)

        if num >= 4:
        	ans = ans + "IV"
        	num = 0
        ans = ans + "I" * num
        
        print(og, num, ans)
        return ans


if __name__ == '__main__':
	s = Solution()
	s.intToRoman(1994)
	s.intToRoman(2470)
	s.intToRoman(2460)
	s.intToRoman(2450)
	s.intToRoman(2440)
	s.intToRoman(3999)
	s.intToRoman(4)
	s.intToRoman(3)
	s.intToRoman(9)
	s.intToRoman(2)
	s.intToRoman(1)
	s.intToRoman(20)
	s.intToRoman(100)
	s.intToRoman(300)
	s.intToRoman(200)

