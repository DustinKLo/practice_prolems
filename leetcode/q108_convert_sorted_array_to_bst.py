# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def dfs(n, arr):
            if len(arr) == 0:
                return None

            if len(arr) == 1:
                mid = 0
            else:
                mid = len(arr) / 2

            n = TreeNode(arr[mid])
            n.left = dfs(n.left, arr[:mid])
            n.right = dfs(n.right, arr[mid + 1:])
            return n

        n = dfs(None, nums)
        return n


if __name__ == '__main__':
    s = Solution()
    s.sortedArrayToBST([-10, -3, 0, 5, 9])

