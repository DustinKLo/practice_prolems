class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in vowels:
                # print('left side', i, s[i])
                while i < j:
                    if s[j] in vowels:
                        # print("right side", j, s[j])
                        temp = s[i]
                        s[i] = s[j]
                        s[j] = temp
                        # print("switched", s)
                        j -= 1
                        break
                    j -= 1
            i += 1
        
        # print(s)
        return ''.join(s)
