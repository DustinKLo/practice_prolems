# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_width = 0
        levels = [] # [[1,1], ...]

        def dfs(node, level, order):
        	if node is None:
        		return

        	if level > len(levels) - 1:
        		levels.append([order, order])
        	else:
        		levels[level][0] = min(levels[level][0], order)
        		levels[level][1] = max(levels[level][1], order)

        	self.max_width = max(self.max_width, levels[level][1] - levels[level][0] + 1)

        	dfs(node.left, level + 1, 2 * order - 1)
        	dfs(node.right, level + 1, 2 * order)

        dfs(root, 0, 1)

        print("ans", self.max_width)
        print("###########################\n")
        return self.max_width


if __name__ == '__main__':
	s = Solution()

	root = TreeNode(1)
	root.left = TreeNode(3)
	root.left.left = TreeNode(5)
	root.left.right = TreeNode(3)
	root.right = TreeNode(2)
	root.right.right = TreeNode(9)
	s.widthOfBinaryTree(root)

	root = TreeNode(1)
	root.left = TreeNode(3)
	root.left.left = TreeNode(5)
	root.left.left.left = TreeNode(6)
	root.right = TreeNode(2)
	root.right.right = TreeNode(9)
	root.right.right.right = TreeNode(7)
	s.widthOfBinaryTree(root)

	root = TreeNode(0)
	s.widthOfBinaryTree(root)
