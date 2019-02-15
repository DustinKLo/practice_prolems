# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, node, total, path_sum):
        if node == None:
            return
        if node.left == None and node.right == None:
            if total + node.val == path_sum:
                self.path_sum = True
            else:
                self.path_sum = self.path_sum or False
        
        self.traverse(node.left, total + node.val, path_sum)
        self.traverse(node.right, total + node.val, path_sum)
                
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.path_sum = False
        self.traverse(root, 0, sum)
        return self.path_sum