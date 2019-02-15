class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # remove spaces and special characters
        s = ''.join(e for e in s if e.isalnum()).lower()
        
        if len(s) == 1:
            return True
        if len(s) == 2:
            if s[0] == s[1]:
                return True
        
        # split string in half reverse other half and check if they're equal
        if len(s) % 2 == 0: # even length string
            mid = len(s) / 2
            if s[:mid] == s[mid:][::-1]:
                return True
            else:
                return False
        else: # odd length string
            mid = len(s) / 2
            if s[:mid] == s[(mid + 1):][::-1]:
                return True
            else:
                return False