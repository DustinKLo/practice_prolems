# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	def __init__(self):
		self.bst_root = None

	def validate_bst(self, node):
		pass

	def maxSumBST(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.validate_bst(root)
		print(self.bst_root.val if self.bst_root else None)


if __name__ == '__main__':
	s = Solution()

	root = TreeNode(1)
	root.left = TreeNode(4)
	root.left.left = TreeNode(2)
	root.left.right = TreeNode(4)
	root.right = TreeNode(3)
	root.right.left = TreeNode(2)
	root.right.right = TreeNode(5)
	root.right.right.left = TreeNode(3)
	root.right.right.right = TreeNode(6)
	# root.right.right.right.right = TreeNode(7)

	s.maxSumBST(root)
