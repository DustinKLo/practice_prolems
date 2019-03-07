"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def __init__(self):
        self.depths = []
        
    def traverse(self, depth, root):
        if root is None:
            return
        # print(depth, root.val, len(self.depths))
        if depth >= len(self.depths):
            self.depths.append([root.val])
        else:
            self.depths[depth].append(root.val)
        
        for child in root.children:
            self.traverse(depth + 1, child)
        
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        self.traverse(0, root)
        # print(self.depths)
        return self.depths
        
        