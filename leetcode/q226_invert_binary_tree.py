# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:
            return
        
        # switching the nodes
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.helper(root.left)
        self.helper(root.right)
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        self.helper(root)
        return root;
        
        