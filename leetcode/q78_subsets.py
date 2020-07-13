class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print(nums)
        ans = [[]]
        
        def traverse(l, s):
            # l is letters left
            # s is ans set
            if len(l) == 0:
                return 

            for i in range(len(l)):
                ans.append(s + [l[i]])
                traverse(l[i + 1:], s + [l[i]])

        traverse(nums, [])
        print(ans)
        print("################################################\n")
        return ans


if __name__ == '__main__':
    """    
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
    """
    s = Solution()
    s.subsets([1,2,3])
    s.subsets([1,1,3])
