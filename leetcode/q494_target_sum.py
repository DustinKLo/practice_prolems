class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        print(nums)
        mem = {}

        def traverse(total, target, i, end):
            if i == end:
                if total == S:
                    return 1
                else:
                    return 0

            if (i, total) in mem:
                return mem[i, total]
            
            left = traverse(total - nums[i], S, i + 1, end)
            right = traverse(total + nums[i], S, i + 1, end)

            mem[i, total] = left + right
            return left + right


        traverse(0, S, 0, len(nums))
        print(mem[0, 0])
        print("####################################\n")
        return mem[0, 0]


if __name__ == '__main__':
    s = Solution()
    s.findTargetSumWays([1,1,1], -1)
    s.findTargetSumWays([1,1,1,1,1], 3)
    s.findTargetSumWays([1,1,1,1,1,1,1], 5)
    s.findTargetSumWays([1,2,3,4,5,4,3,2,5], 15)
    s.findTargetSumWays([50,37,6,20,35,41,45,3,20,36,49,1,20,10,43,4,44,15,44,34], 25)
    s.findTargetSumWays([34,16,5,38,20,20,8,43,3,46,24,12,28,19,22,28,9,46,25,36], 0)
