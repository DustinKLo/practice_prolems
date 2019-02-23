class Solution(object):
    def letter_count(self, string):
        letters = {}
        for ch in string:
            if ch not in letters:
                letters[ch] = 1
            else:
                letters[ch] += 1
        return letters
    
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        letters_s = self.letter_count(s)
        letters_t = self.letter_count(t)
        
        for key in letters_s.keys():
            if letters_s[key] != letters_t.get(key):
                return False
        return True

