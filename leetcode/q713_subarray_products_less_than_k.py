class Solution(object):
    @staticmethod
    def print_mem_tbl(nums, tbl):
        nums_row = [str(i) for i in nums]
        print('\t' + '\t'.join(nums_row))
        for j in range(len(tbl)):
            # print(nums[j], tbl[j])
            row = str(nums[j]) + '\t' + '\t'.join(str(i) for i in tbl[j])
            print(row)

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mem_tbl = [[0] * len(nums) for i in range(len(nums))]

        l = 0  # left bound
        r = 0  # right bound, will increment by 1 after every outer loop

        ans = []
        count = 0

        while r - l < len(nums):  # outer loop
            i = l
            j = r
            while j < len(nums):  # inner loop
                if j - i == 0:
                    if nums[i] < k:
                        ans.append([nums[i]])
                        count += 1
                    mem_tbl[i][j] = nums[i]
                else:
                    prod = mem_tbl[i][j - 1] * nums[j]
                    if prod < k:
                        ans.append(nums[i:j + 1])
                        count += 1
                    mem_tbl[i][j] = prod
                i += 1
                j += 1
            r += 1

        # self.print_mem_tbl(nums, mem_tbl)
        print(ans)
        print(count)
        return count


if __name__ == '__main__':
    s = Solution()

    s.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
