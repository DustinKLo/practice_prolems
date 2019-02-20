class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cache = {}
        
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            # print("not Isomorphic")
            return False
    
        for i in range(len(s)):
            word_1_letter = s[i]
            word_2_letter = t[i]
            # print(word_1_letter, word_2_letter)
            
            if s[i] not in cache:
                cache[word_1_letter] = t[i]
                # print("added to cache", cache)
            else:
                if word_2_letter != cache[word_1_letter]:
                    return False
        
        # print(cache)
        return True
        