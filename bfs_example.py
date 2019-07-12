# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def spiral_tree(root):
	queue = []

	def traverse(node, direction):
		queue.append(node)
		
		while len(queue) > 0:
			if len(queue) > 0:
				print([x.val for x in queue if x is not None])
			cur_node = queue.pop(0)
			if cur_node:
				print(cur_node.val)
				if direction == 1:
					queue.append(cur_node.left)
					queue.append(cur_node.right)
				else:
					queue.append(cur_node.right)
					queue.append(cur_node.left)
			direction *= -1
	
	traverse(root, -1)


if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(7)

	spiral_tree(root)

