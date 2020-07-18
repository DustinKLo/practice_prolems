# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def dfs(self, node):
        if node is None:
            return []

        if node.left is None and node.right is None:
            return [node.val]
        
        return self.dfs(node.left) + self.dfs(node.right)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        l1 = self.dfs(root1)
        l2 = self.dfs(root2)
        return True if l1 == l2 else False
