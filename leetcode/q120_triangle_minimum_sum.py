# DP problem, similar to Q64, minimum sum path

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        # add along the edges, index 0 and last index
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]

        for r in triangle:
            print(r)

        if len(triangle) > 2:
            for j in range(2, len(triangle)):
                for i in range(1, len(triangle[j]) - 1):
                    # j row
                    # i column
                    opt1 = triangle[j][i] + triangle[j-1][i-1]
                    opt2 = triangle[j][i] + triangle[j-1][i]
                    triangle[j][i] = min(opt1, opt2)
        last_row = triangle[len(triangle) - 1]
        return min(last_row)

if __name__ == '__main__':
    s = Solution()
    t1 = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    s.minimumTotal(t1)
