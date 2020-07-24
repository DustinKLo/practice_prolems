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
        depths = []
        def dfs(node, depth, order):
            if node is None:
                return
            
            if depth > len(depths) - 1:
                depths.append([node.val])
            else:
                if order == 1:
                    depths[depth].append(node.val)
                else:
                    depths[depth].insert(0, node.val)
            dfs(node.left, depth + 1, order * -1)
            dfs(node.right, depth + 1, order * -1)
        
        dfs(root, 0, 1)
        for d in depths:
            print(d)
        print("##################\n")
        return depths

    def zigzagLevelOrderBFS(self, root):
        if root is None:
            return []

        cur_row = [root]
        next_row = []

        rows = []
        order = 1

        while len(cur_row) > 0:
            cur_row_len = len(cur_row)
            row = []

            while cur_row_len > 0:
                node = cur_row.pop(-1)
                row.append(node.val)

                if order == 1:
                    next_row.append(node.left) if node.left else None
                    next_row.append(node.right) if node.right else None
                else:
                    next_row.append(node.right) if node.right else None
                    next_row.append(node.left) if node.left else None

                cur_row_len -= 1

            rows.append(row)
            cur_row = next_row
            next_row = []
            order *= -1

        for r in rows:
            print(r)
        print("##################\n")
        return rows


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s.zigzagLevelOrder(root)
    s.zigzagLevelOrderBFS(root)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)
    s.zigzagLevelOrder(root)
    s.zigzagLevelOrderBFS(root)
