class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapper = {
			"I": 1,
			"V": 5,
			"X": 10,
			"L": 50,
			"C": 100,
			"D": 500,
			"M": 1000,
        }
        
        i = 0
        ans = 0
        while i < len(s):
        	c = s[i]
        	val = mapper[c]
        	if i + 1 < len(s):
        		next_c = s[i + 1]
        		next_val = mapper[next_c]
        		if val < next_val:
        			ans = ans + next_val - val
        			i += 2
        		else:
        			ans = ans + val
        			i += 1
        	else:  # reached end
        		ans = ans + val
        		i += 1

        print(ans)
        return ans

if __name__ == '__main__':
	s = Solution()
	s.romanToInt("III")
	s.romanToInt("IV")
	s.romanToInt("IX")
	s.romanToInt("LVIII")
	s.romanToInt("MCMXCIV")
	s.romanToInt("MMMCMXCIX")
