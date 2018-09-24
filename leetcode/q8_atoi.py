
def myAtoi(s):
    """
    :type str: str
    :rtype: int
    """
    INT_MAX =  2147483647
    INT_MIN = -2147483648
    
    sign = 1
    
    s = s.strip()

    if s[0] == "+":
    	sign = 1
    	s = s[1:]
    elif s[0] == "-":
    	sign = -1
    	s = s[1:]

    if ord(s[0]) < 48 and ord(s[0]) > 57:
    	return 0

    ans = ''
    for ch in s:
    	if 48 <= ord(ch) <= 57:
    		ans += ch
    	else:
    		break

    if len(ans) >= 1:
    	return int(ans) * sign
    else:
    	return 0


if __name__ == '__main__':
	s = ' 7 -36178 djskda '
	ans = myAtoi(s)
	print(ans)
