# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# better solution is to use a self.max vairable and compare it
# max(self.max, depth) for every iteration (recursive step)
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depths = []
        def traverse(node, depth):
            if node != None:
                if len(depths) - 1 < depth:
                    depths.append(0)
                
                traverse(node.left, depth + 1)
                traverse(node.right, depth + 1)
        
        traverse(root, 0)
        print len(depths)
        return len(depths)
        