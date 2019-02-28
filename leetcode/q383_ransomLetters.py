class Solution(object):
    def letterCount(self, string):
        # print(string)
        letters = {}
        for ch in string:
            if ch not in letters.keys():
                letters[ch] = 1
            else:
                letters[ch] += 1
        return letters
        
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomLetters = self.letterCount(ransomNote)
        magazineLetters = self.letterCount(magazine)
        
        for ch, count in ransomLetters.iteritems():
            if count > magazineLetters.get(ch, 0):
                return False
        
        return True
