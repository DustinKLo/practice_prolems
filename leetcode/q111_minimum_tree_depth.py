# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, node, depth):
        if node == None:
            return
        
        if node.left == None and node.right == None:
            self.min_depth = min(self.min_depth, depth)
        
        self.traverse(node.left, depth + 1)
        self.traverse(node.right, depth + 1)
    
    def minDepth(self, root):
        self.min_depth = float('inf')
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        self.traverse(root, 0)
        return self.min_depth + 1
        