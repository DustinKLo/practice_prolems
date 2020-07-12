class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []

        ls = list(range(1, n + 1))
        ans = []
        print(ls, k)
        
        def traverse(l, c, target):
            # l is values left
            # c is answer set
            # k is target
            if len(c) == target:
                ans.append(c)
                return 

            for i in range(0, len(l)):
                traverse(l[i + 1:], c + [l[i]], target)
                
        traverse(ls, [], k)

        for a in ans:
            print(a)
        print("###########################\n")
        return ans


if __name__ == '__main__':
    s = Solution()
    s.combine(4, 2)
