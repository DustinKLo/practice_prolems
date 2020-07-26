# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.ans = 0

    def get_sum_path(self, node, val, target):
        if node is None:
            return 0
        if val + node.val == target:
            self.ans += 1
        
        return self.get_sum_path(node.left, val + node.val, target) + \
               self.get_sum_path(node.right, val + node.val, target)
    
    def dfs(self, node, target):
        if node is None:
            return
        self.get_sum_path(node, 0, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.ans = 0
        self.dfs(root, sum)
        return self.ans
        