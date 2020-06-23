class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        print(digits)
        digits = str(digits)
        mapper = {
        	'1': '',
        	'2': 'abc',
        	'3': 'def',
        	'4': 'ghi',
        	'5': 'jkl',
        	'6': 'mno',
        	'7': 'pqrs',
        	'8': 'tuv',
        	'9': 'wxyz',
        }

        if digits == "":
            return []        

        ans = []
        def traverse(nums, res):
        	if len(nums) == 0:
        		ans.append(res)
        		return

        	num = nums[0]
        	if num == '1':
        		traverse(nums[1:], res)
        	else:
	        	for ch in mapper[num]: # ex. 'abc'
	        		traverse(nums[1:], res + ch)

        traverse(digits, "")
        print(ans)
        return ans


if __name__ == '__main__':
	s = Solution()
	s.letterCombinations(626321)
	s.letterCombinations("")
	s.letterCombinations(123456789)
