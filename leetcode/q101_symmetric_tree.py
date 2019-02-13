# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):   
    def traverse(self, left_side, right_side):
        if left_side == None and right_side == None:
            return
        # if left_side != None and right_side != None:
        #     print("left side: {}\nright side: {}".format(left_side.val, right_side.val))
        #     print(left_side.val == right_side.val)
        #     print("\n")
        if (left_side == None) ^ (right_side == None):
            self.symmetric = False
            return
        if left_side.val != right_side.val:
            self.symmetric = False
            return
        
        # print(left_side.right, right_side.left)
        self.traverse(left_side.left, right_side.right)
        self.traverse(left_side.right, right_side.left)
        
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.symmetric = True
        
        if not root:
            return True
        elif root.left == None and root.right == None:
            return True
        elif (root.left == None) ^ (root.right == None):
            return False
        
        else:
            left_side = root.left
            right_side = root.right

            self.traverse(left_side, right_side)
            # print(self.symmetric)

            return self.symmetric
