# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.paths = []
        
    def traverse(self, root, path):
        if root == None:
            return
        
        left_path = path + [root.left.val] if root.left != None else path
        right_path = path + [root.right.val] if root.right != None else path
        
        if root.left == None and root.right == None:
            self.paths.append(path)
            
        self.traverse(root.left, left_path)
        self.traverse(root.right, right_path)
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        
        self.traverse(root, [root.val])
        return ["->".join(str(p) for p in path) for path in self.paths]
