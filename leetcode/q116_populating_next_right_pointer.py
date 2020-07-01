# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.depths = []

        def traverse(node, depth):
            if node is None:
                return

            if depth >= len(self.depths):
                self.depths.append([node])
            else:
                self.depths[depth].append(node)

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)

        if len(self.depths) == 0:
            return root

        for row in self.depths:
            if len(row) == 1:
                continue
            i = 0
            j = i + 1
            while j < len(row):
                print(row[i].val, " -> ", row[j].val )
                row[i].next = row[j]
                i += 1
                j += 1
        return root


if __name__ == '__main__':
    s = Solution()

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    s.connect(root)
