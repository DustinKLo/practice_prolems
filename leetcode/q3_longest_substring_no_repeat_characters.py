class Solution(object):
	def lengthOfLongestSubstringSlow(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# if len(set([ch for ch in s])) == 1:
		# 	return 1

		seen_letters = set()
		longest_string = 0

		for i in range(0, len(s)):
			for j in range(i, len(s)):
				char = s[j]
				print(i, j, char, s[i:j+1], seen_letters, longest_string)
				if char in seen_letters:
					# print("seen!\n")
					break
				else:
					str_len = j - i + 1
					if str_len > longest_string:
						print("setting longest string: ", str_len)
						longest_string = str_len
				seen_letters.add(char)

			seen_letters = set()
		print("ANSWER longest_string: ", longest_string)
		return longest_string

	def lengthOfLongestSubstring(self, s):
		n = len(s)
		i = 0  # left window
		j = 0  # right window

		longest_string = 0
		seen_letters = set()
		
		while i < n and j < n:
			char = s[j]
			print(i, j, s[i], s[j], s[i:j+1])

			if char not in seen_letters:
				seen_letters.add(char)
				# j - i + 1 is the length of the substring
				if j - i + 1 > longest_string:
					longest_string = j - i + 1
				j += 1
			else:
				seen_letters.remove(s[i])
				i += 1

		print("ANSWER longest_string: ", longest_string)
		return longest_string



if __name__ == '__main__':
	s = Solution()
	s.lengthOfLongestSubstringSlow("abcabcbb")
	print("#########\n")
	s.lengthOfLongestSubstringSlow("bbbbb")
	print("#########\n")
	s.lengthOfLongestSubstringSlow("pwwkew")
	print("#########\n")
	s.lengthOfLongestSubstringSlow("au")
	print("#########\n")
	s.lengthOfLongestSubstring("abcabcbb")
	print("#########\n")
	s.lengthOfLongestSubstring("bbbbb")
	print("#########\n")
	s.lengthOfLongestSubstring("pwwkew")
	print("#########\n")
	s.lengthOfLongestSubstring("au")
	print("#########\n")
