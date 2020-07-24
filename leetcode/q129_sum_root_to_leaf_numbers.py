# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, v):
            if node is None:
                return 0

            leaf_val = v * 10 + node.val
            print(node.val, leaf_val)

            if node.left is None and node.right is None:
                return leaf_val

            return dfs(node.left, leaf_val) + dfs(node.right, leaf_val)

        ans = dfs(root, 0)
        print(ans)
        print("###################################\n")
        return ans


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(4)
    root.left = TreeNode(9)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    root.right = TreeNode(0)
    s.sumNumbers(root)
