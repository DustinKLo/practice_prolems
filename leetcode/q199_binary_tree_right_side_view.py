# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		self.depths = -1
		values = []
		x_axes = []
		def traverse(node, depth, axis):
			if node is None:
				return

			print(node.val, depth, axis)
			if depth > self.depths:
				self.depths += 1
				values.append(node.val)
				x_axes.append(axis)

			if axis >= x_axes[depth]:
				values[depth] = node.val

			traverse(node.left, depth + 1, axis - 1)
			traverse(node.right, depth + 1, axis + 1)

		traverse(root, 0, 0)
		print("values", values)
		print("########################\n")
		return values

		
if __name__ == '__main__':
	s = Solution()

	root = TreeNode(1)
	root.left = TreeNode(2)
	root.left.right = TreeNode(5)
	root.right = TreeNode(3)
	root.right.right = TreeNode(4)
	s.rightSideView(root)

	root = TreeNode(1)
	root.left = TreeNode(2)
	root.left.right = TreeNode(5)
	root.right = TreeNode(3)
	root.right.left = TreeNode(6)
	s.rightSideView(root)	
