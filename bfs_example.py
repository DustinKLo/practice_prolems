# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def spiral_tree(root):
	current_level = [root]  # stacks
	next_level = []  # stacks

	direction = -1
	while len(current_level) > 0 or len(next_level) > 0:
		while len(current_level) > 0:
			cur_node = current_level.pop(-1)
			print(cur_node.val)

			if direction == 1:
				next_level.append(cur_node.left) if cur_node.left else None
				next_level.append(cur_node.right) if cur_node.right else None
			else:
				next_level.append(cur_node.right) if cur_node.right else None
				next_level.append(cur_node.left) if cur_node.left else None
		current_level = next_level
		next_level = []
		direction *= -1


def spiral_tree_inefficient(root):
	node_layers = []
	
	def traverse(node, level):
		if node is None:
			return
		if len(node_layers) <= level:
			node_layers.append([node.val])
		else:
			node_layers[level].append(node.val)
		traverse(node.left, level + 1)
		traverse(node.right, level + 1)

	traverse(root, 0)
	switch = -1
	for layer in node_layers:
		if switch == 1:
			print(layer)
		else:
			layer.reverse()
			print(layer)
		switch *= -1
		


if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(7)

	spiral_tree(root)
	spiral_tree_inefficient(root)

