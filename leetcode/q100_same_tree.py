# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # depth verse search helper function
    def traverseTree(self, node, l):
        if node == None:
            l.append(None)
            return

        l.append(node.val)
        self.traverseTree(node.left, l)
        self.traverseTree(node.right, l)
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        l1 = []
        l2 = []
        self.traverseTree(p, l1)
        self.traverseTree(q, l2)
        
        print(l1)
        print(l2)
        
        if l1 == l2:
            return True
        else:
            return False
        