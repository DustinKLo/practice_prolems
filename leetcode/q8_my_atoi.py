class Solution(object):
    def myAtoi(self, word):
        """
        :type str: str
        :rtype: int
        """
        allowed_chars = ['1','2','3','4','5','6','7','8','9','0']
        MAX_VALUE = 2147483647
        MIN_VALUE = -2147483648

        ans = 0
        sign = 1
        start = 0

        word = word.strip()
        if word == "":
        	return 0
        
        if word[0] == '-':
        	sign = -1
        	start = 1
        elif word[0] == '+':
        	start = 1

        for i in range(start, len(word)):
        	if word[i] not in allowed_chars:
        		break
        	else:
        		ans = (ans * 10) + int(word[i])

    	ans = sign * ans
    	if ans > MAX_VALUE:
    		return MAX_VALUE
    	elif ans < MIN_VALUE:
    		return MIN_VALUE
    	else:
    		return ans
        

if __name__ == '__main__':
	s = Solution()
	print(s.myAtoi("    -4193 with words"))
	print("")
	print(s.myAtoi("words and 987"))
	print("")
	print(s.myAtoi("-91283472332"))
	print("")
	print(s.myAtoi("4193 with words"))
	print("")
	print(s.myAtoi("   -42"))
	print("")
	print(s.myAtoi("-2147483648"))