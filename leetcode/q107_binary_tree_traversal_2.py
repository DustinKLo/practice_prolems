# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Probably better to use BFS since DFS will put the node-levels in order from top to bottom
class Solution(object):
    def traverse(self, node, depth):
        # print(self.level)
        if node == None:
            return
        
        # append to self.level at the start of every depth
        if len(self.level) <= depth:
            # append to the list
            self.level.append([])

        self.traverse(node.left, depth + 1)
        self.traverse(node.right, depth + 1)
        self.level[depth].append(node.val)
        
    
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.level = []
        self.traverse(root, 0)
        self.level.reverse()
        return self.level
        