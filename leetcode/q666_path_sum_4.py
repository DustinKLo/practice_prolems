# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def parse_values(n):
        val = n % 10  # get val
        n = n // 10

        order = n % 10  # get order
        n = n // 10

        depth = n % 10  # get depth
        n = n // 10

        return depth, order, val

    def dfs(self, node, val):
        if node is None:
            return

        if node.left is None and node.right is None:
            self.ans += val + node.val

        self.dfs(node.left, val + node.val)
        self.dfs(node.right, val + node.val)


    def pathSum(self, nums):
        depth, order, val = self.parse_values(nums[0])  # initializing tree
        root = TreeNode(val)

        if len(nums) == 1:
        	return val

        for i in range(1, len(nums)):
            num = nums[i]
            depth, order, val = self.parse_values(num)

            left = 1
            right = 2 ** (depth - 1)

            node = TreeNode(val)
            cur = root
            while left < right:
                mid = (left + right) // 2
                if order > mid:  # go right
                    left = mid + 1
                    if cur.right is not None:
                        cur = cur.right
                    else:
                        cur.right = node
                else:  # go left
                    right = mid
                    if cur.left is not None:
                        cur = cur.left
                    else:
                        cur.left = node

        self.ans = 0
        self.dfs(root, 0)
        print("ans", self.ans)
        print("####################################\n")
        return self.ans


if __name__ == '__main__':
    s = Solution()
    s.pathSum([113, 215, 221, 321, 332, 433, 454])  # 22
    s.pathSum([113, 215, 221])  # 12
    s.pathSum([113, 221])  # 4
