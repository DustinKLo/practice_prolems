# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path_sum = float('-inf')
        def dfs(node):
            if node is None:
                return 0

            if node.val > self.max_path_sum:
                self.max_path_sum = node.val

            left = dfs(node.left)
            right = dfs(node.right)

            best_sum = max(node.val + left + right, node.val + left, node.val + right)
            if best_sum > self.max_path_sum:
                self.max_path_sum = best_sum

            return max(node.val, node.val + left, node.val + right)
        dfs(root)
        print(self.max_path_sum)
        print("########################\n")
        return self.max_path_sum


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s.maxPathSum(root)

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s.maxPathSum(root)

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    s.maxPathSum(root)    
