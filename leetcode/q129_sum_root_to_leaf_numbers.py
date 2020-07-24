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
        self.ans = 0
        def dfs(node, v):
            if node is None:
                return

            leaf_val = v * 10 + node.val
            print(node.val, leaf_val)

            if node.left is None and node.right is None:
                self.ans += leaf_val
                return
            
            dfs(node.left, leaf_val)
            dfs(node.right, leaf_val)
        dfs(root, 0)
        print(self.ans)
        print("########################\n")
        return self.ans


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(4)
    root.left = TreeNode(9)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    root.right = TreeNode(0)
    s.sumNumbers(root)
