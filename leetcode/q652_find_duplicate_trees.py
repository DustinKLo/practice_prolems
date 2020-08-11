# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # self.sub_tree_vals = []
        self.counts = {}
        self.ans = []
        
        def dfs(node):
            if node is None:
                return [None]
            
            left = dfs(node.left)
            right = dfs(node.right)

            str_hash = str(left + [node.val] + right)
            
            if str_hash not in self.counts:
                self.counts[str_hash] = 1
            elif self.counts[str_hash] == 1:
                self.counts[str_hash] += 1
                self.ans.append(node)

            return left + [node.val] + right

        dfs(root)

        for k in self.counts:
        	print(k, self.counts[k])

        print(self.ans)
        print("#########################\n")
        return self.ans


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(4)
    root.right.right = TreeNode(4)
    s.findDuplicateSubtrees(root)

    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.right = TreeNode(0)
    root.right.right = TreeNode(0)
    root.right.right.right = TreeNode(0)
    s.findDuplicateSubtrees(root)
