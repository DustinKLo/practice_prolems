# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.lowest_parent = None

    def traverse(self, node, p, q):
        if node == None:
            return False
        print('current node: %s' % node.val)

        if node.val == p or node.val == q:
            print('found it: %s' % node.val)
            self.lowest_parent = node.val
            return True

        left = self.traverse(node.left, p, q)
        right = self.traverse(node.right, p, q)

        if left == True and right == True:
            self.lowest_parent = node.val
            return True

        if left ^ right:
            return True
        return False

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.traverse(root, p, q)
        return self.lowest_parent


if __name__ == '__main__':
    import random

    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.left.right.left = TreeNode(9)
    root.right.left.right.right = TreeNode(10)
    root.right.left.right.left.left = TreeNode(11)
    root.right.left.right.left.left.right = TreeNode(12)
    root.right.right = TreeNode(6)
    
    # Leetcode example tree
    # root = TreeNode(3)
    # root.left = TreeNode(5)
    # root.left.left = TreeNode(6)
    # root.left.right = TreeNode(2)
    # root.left.right.left = TreeNode(7)
    # root.left.right.right = TreeNode(4)
    # root.right = TreeNode(1)
    # root.right.left = TreeNode(0)
    # root.right.right = TreeNode(8)

    s = Solution()
    for i in range(0, 25):
        node_list = set(list(range(0, 12)))
        child1 = random.sample(node_list, 1)[0]
        node_list.remove(child1)
        child2 = random.sample(node_list, 1)[0]
        print('child nodes [%s, %s]' % (child1, child2))
        lowest_parent = s.lowestCommonAncestor(root, child1, child2)
        print('LOWEST PARENT: %s' % lowest_parent)
        print('#' * 25 + '\n')
