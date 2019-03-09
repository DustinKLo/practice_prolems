# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.paths = []
        
    def traverse(self, root, path, target):
        # root: node
        # path: List[int]
        if root == None:
            return

        path_extend = path + [root.val] # adding to path
        if root.val + sum(path) == target and root.left == None and root.right == None:
            return self.paths.append(path_extend)
        self.traverse(root.left, path_extend, target)
        self.traverse(root.right, path_extend, target)
        
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.traverse(root, [], sum)
        return self.paths
