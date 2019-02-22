# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


# get path of node https://www.geeksforgeeks.org/print-path-root-given-node-binary-tree/
class Solution(object):
	def find_path(self, root, target, path):
		if root == None:
			return False

		path.append(root.val)
		if root.val == target.val:
			return True
		
		if self.find_path(root.left, target, path) or self.find_path(root.right, target, path):
			return True
		
		path.pop(-1)
		return False


	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		self.path1 = []
		self.path2 = []
		
		path1 = self.find_path(root, p, self.path1)
		print(self.path1)
		path2 = self.find_path(root, q, self.path2)
		print(self.path2)

		i, j = 0, 0
		while i < len(self.path1) and j < len(self.path2):
			if self.path1[i] == self.path2[j]:
				i += 1; j += 1
			else: 
				break
		print(self.path1[i - 1])
		return self.path1[i - 1]



if __name__ == "__main__":
	root = TreeNode(3)
	root.left = TreeNode(5)
	root.right = TreeNode(1)
	root.left.left = TreeNode(6)
	root.left.right = TreeNode(2)
	root.left.right.left = TreeNode(7)
	root.left.right.right = TreeNode(4)
	# root.left.right.right.right = TreeNode(9)
	# root.left.right.right.right.right = TreeNode(10)
	# root.left.right.right.right.right.right = TreeNode(11)
	root.right = TreeNode(1)
	root.right.left = TreeNode(0)
	root.right.right = TreeNode(8)
	Solution().lowestCommonAncestor(root, TreeNode(4), TreeNode(6))



