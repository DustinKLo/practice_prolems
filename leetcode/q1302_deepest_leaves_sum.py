# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # def __init__(self):
    #     self.deepest_depth = -1
    #     self.sum = float('-inf')
    def traverse(self, node, depth):
        if node is None:
            return

        if depth == self.deepest_depth:
            self.sum = self.sum + node.val

        if depth > self.deepest_depth:
            self.sum = node.val
            self.deepest_depth = depth

        print(depth, node.val, self.sum)

        self.traverse(node.left, depth + 1)
        self.traverse(node.right, depth + 1)

    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.deepest_depth = -1
        self.sum = 0

        self.traverse(root, 0)
        print("deepest leaves sum:", self.sum)
        return self.sum


if __name__ == '__main__':
    s = Solution()
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(6)
    root.right.right.right = TreeNode(8)
    s.deepestLeavesSum(root)
