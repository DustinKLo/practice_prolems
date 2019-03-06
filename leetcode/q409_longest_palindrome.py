class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for ch in s:
            if ch not in letters.keys():
                letters[ch] = 1
            else:
                letters[ch] += 1
        
        odd_letter_count = 0
        longest_palindrome_length = 0
        for k, v in letters.iteritems():
            longest_palindrome_length += (v if v % 2 == 0 else v - 1)
            if v % 2 != 0:
                odd_letter_count += 1
        
        if odd_letter_count > 0:
            return longest_palindrome_length + 1
        else:
            return longest_palindrome_length
