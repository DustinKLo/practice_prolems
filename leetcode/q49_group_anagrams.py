class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_tbl = {}
        for word in strs:
        	key = ''.join(sorted(word))
        	if key not in hash_tbl:
        		hash_tbl[key] = [word]
        	else:
        		hash_tbl[key].append(word)

        ans = []
        for key, item in hash_tbl.items():
        	ans.append(item)

        print(ans)
        return ans


if __name__ == '__main__':
	s = Solution()
	s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

