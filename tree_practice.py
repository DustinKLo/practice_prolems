# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.valid = True

    def traverse_validate(self, root, direction):
        # direction: "left", "right"
        # root: TreeNode object
        if root is None:
            return [], [] # return empty arrays (right side and left side) for base case

        left_left, left_right = self.traverse_validate(root.left, "left")
        right_left, right_right = self.traverse_validate(root.right, "right")

        all_left_nodes = left_left + left_right
        all_right_nodes = right_left + right_right

        max_left_side = max(all_left_nodes) if len(all_left_nodes) > 0 else float('-inf')
        min_right_side = min(all_right_nodes) if len(all_right_nodes) > 0 else float('inf')

        print("Current node value: {}".format(root.data))
        print("Left Array: {}".format(all_left_nodes))
        print("Right Array: {}".format(all_right_nodes))

        if root.data > min_right_side or root.data < max_left_side:
            print("Not a valid binary search tree\n")
            self.valid = False
            # return [], [] # break the loop if its invalid
        else:
            print("IS a valid binary search tree\n")

        if direction == "right":
            all_right_nodes.append(root.data)
        elif direction == "left":
            all_left_nodes.append(root.data)

        return all_left_nodes, all_right_nodes

    def validate(self):
        self.traverse_validate(self, "")
        print(self.valid)
        return self.valid


if __name__ == "__main__":
    a1 = TreeNode(20);
    a1.left = TreeNode(10);
    a1.left.left = TreeNode(5);
    a1.left.right = TreeNode(15);
    a1.left.right.left = TreeNode(12);
    a1.left.right.right = TreeNode(16);
    a1.left.left.left = TreeNode(1);
    a1.left.left.right = TreeNode(6);
    a1.right = TreeNode(30);
    a1.right.left = TreeNode(25);
    a1.right.left.left = TreeNode(5);
    a1.right.right = TreeNode(35);
    a1.right.right.left = TreeNode(10);
    a1.right.right.right = TreeNode(40);
    a1.right.right.right.right = TreeNode(45);
    a1.right.right.right.right.right = TreeNode(50);
    a1.validate()
