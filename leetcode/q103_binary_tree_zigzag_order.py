# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        queue = []
        queue.append(root)  # enqueue
        
        levels = []
        order = 1
        
        while len(queue) > 0:
            queue_len = len(queue)
            level = []

            while queue_len > 0:
                if order == 1:
                    node = queue.pop(0)
                else:
                    node = queue.pop(-1)
                level.append(node.val)

                if order == -1:
                    if node.left:
                        queue.insert(0, node.left)
                    if node.right:
                        queue.insert(0, node.right)
                else:
                    if node.right:
                        queue.insert(0, node.right)
                    if node.left:
                        queue.insert(0, node.left)
                queue_len -= 1

            levels.append(level)
            order *= -1

        for l in levels:
            print(l)
        print("########################\n")
        return levels


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s.zigzagLevelOrder(root)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)
    s.zigzagLevelOrder(root)
