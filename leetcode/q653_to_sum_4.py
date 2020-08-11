# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        vals = set()
        self.ans = False
        
        def dfs(node):
            if node is None:
                return
            
            # if node.val not in set
            target_val = k - node.val
            if target_val in vals:
                self.ans = True
            vals.add(node.val)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.ans
