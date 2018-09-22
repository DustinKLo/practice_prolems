
def check_palindrome(s):
	pass

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    print s

    for i in range(0, len(s)-1):
    	sub_string = s[i:]
    	print '{} {} {}'.format(i, s[i], s[i:])

longestPalindrome("babadsqujandz")
