# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ValidBinarySearchTree:
    def __init__(self):
        self.valid = True

    def traverse(self, node, min_val, max_val):
    	if node is None:
    		return None

    	if node.val <= min_val or node.val >= max_val:
    		self.valid = False

    	print(node.val, min_val, max_val)
        self.traverse(node.left, min_val, node.val)
        self.traverse(node.right, node.val, max_val)


    def solution(self, root):
        self.traverse(root, -float("inf"), float("inf"))
        return self.valid



if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right = TreeNode(10)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    s = ValidBinarySearchTree()
    print(s.solution(root))
    print("")

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(12)
    s = ValidBinarySearchTree()
    print(s.solution(root))
    print("")

