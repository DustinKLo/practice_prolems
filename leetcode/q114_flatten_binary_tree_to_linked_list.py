# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
        	return

        self.ls = []

        def dfs(node):
            if node is None:
                return
            self.ls.append(node)
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        if len(self.ls) == 1:
        	return root

        for i in range(0, len(self.ls)):
            self.ls[i].left = None
            if i == len(self.ls) - 1:
                self.ls[i].right = None
            else:
                self.ls[i].right = self.ls[i + 1]


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    s.flatten(root)
