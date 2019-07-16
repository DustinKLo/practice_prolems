# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'https://medium.com/@codingfreak/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f'

def spiral_tree(root):
    current_level = [root]  # stacks
    next_level = []  # stacks

    direction = -1
    ans = ''
    while len(current_level) > 0 or len(next_level) > 0:
        while len(current_level) > 0:
            cur_node = current_level.pop(-1)
            ans += '%i, ' % cur_node.val

            if direction == 1:
                next_level.append(cur_node.left) if cur_node.left else None
                next_level.append(cur_node.right) if cur_node.right else None
            else:
                next_level.append(cur_node.right) if cur_node.right else None
                next_level.append(cur_node.left) if cur_node.left else None
        current_level = next_level
        next_level = []
        direction *= -1
    print(ans)


def reverse_order_tree(root):
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
    for i in range(len(node_layers), 0, -1):
        print(node_layers[i-1])


def reverse_order_tree_iterative(root):
    current_level = [root]  # stacks
    next_level = []  # stacks

    direction = -1
    ans = [root]
    while len(current_level) > 0 or len(next_level) > 0:
        while len(current_level) > 0:
            cur_node = current_level.pop(0)
            next_level.append(cur_node.left) if cur_node.left else None
            next_level.append(cur_node.right) if cur_node.right else None
        ans = next_level + ans
        current_level = next_level
        next_level = []
        direction *= -1
    print([n.val for n in ans])


def specific_order_print_node(root):
    queue1 = [root.left]  # .append() to enqueue, .pop(0) to dequeue
    queue2 = [root.right]

    ans = []
    if root is not None:
        ans.append(root.val)
    while len(queue1) > 0 or len(queue2) > 0:
        while len(queue1) > 0:
            x = queue1.pop(0)
            ans.append(x.val)
            queue1.append(x.left) if x.left is not None else None
            queue1.append(x.right) if x.right is not None else None

            y = queue2.pop(0)
            ans.append(y.val)
            queue2.append(y.right) if y.right is not None else None
            queue2.append(y.left) if y.left is not None else None
    print(ans)


def left_view_tree(root):
    current_level = [root]
    next_level = []

    ans = []
    ans.append(root.val) if root is not None else None

    while len(current_level) > 0 or len(next_level) > 0:
        while len(current_level) > 0:
            n = current_level.pop(0)
            next_level.append(n.left) if n.left is not None else None
            next_level.append(n.right) if n.right is not None else None
        ans.append(next_level[0].val) if len(next_level) > 0 else None
        current_level = next_level
        next_level = []
    print(ans)


def right_view_tree(root):
    current_level = [root]
    next_level = []

    ans = []
    ans.append(root.val) if root is not None else None

    while len(current_level) > 0 or len(next_level) > 0:
        while len(current_level) > 0:
            n = current_level.pop(0)
            next_level.append(n.left) if n.left is not None else None
            next_level.append(n.right) if n.right is not None else None
        ans.append(next_level[-1].val) if len(next_level) > 0 else None
        current_level = next_level
        next_level = []
    print(ans)


def top_view_tree(root):
    x_axis_hash = set()
    ans = []

    def traverse(node, x_axis):
        if not node:
            return
        if x_axis not in x_axis_hash:
            ans.append(node.val)
            x_axis_hash.add(x_axis)
        traverse(node.left, x_axis - 1)
        traverse(node.right, x_axis + 1)
    traverse(root, 0)
    print(ans)


def bottom_view_tree(root):
    x_axis_hash = {}  # { -1: [node.val, ...], ... }

    def traverse(node, x_axis):
        if not node:
            return
        if x_axis not in x_axis_hash.keys():
            x_axis_hash[x_axis] = [node.val]
        else:
            x_axis_hash[x_axis].append(node.val)
        traverse(node.left, x_axis - 1)
        traverse(node.right, x_axis + 1)
    traverse(root, 0)
    ans = [x_axis_hash[axis][-1] for axis in x_axis_hash.keys()]
    print(ans)


def find_next_node_to_right(root, target):
    node_layers = []

    def traverse(node, level):
        if not node:
            return
        if len(node_layers) <= level:
            node_layers.append([node.val])
        else:
            node_layers[level].append(node.val)
        traverse(node.left, level + 1)
        traverse(node.right, level + 1)
    traverse(root, 0)

    for layer in node_layers:
        try:
            target_index = layer.index(target)
            if target_index > len(layer) - 1:
                return None
            else:
                return layer[target_index + 1]
        except:
            continue


def is_complete_tree(root):
    if not root:
        return True
    # print(root.left.val if root.left else None, root.right.val if root.right else None)
    if not root.left and root.right:
        return False
    return is_complete_tree(root.left) and is_complete_tree(root.right)
    

class TreeCousinChecker():
    def __init__(self, root):
        self.root = root
        self.parent = None
        self.are_cousins = False

    def check_nodes_are_cousins(self, target1, target2):
        print('node values: {} {}'.format(target1, target2))

        def traverse(node, level):
            if not node:
                return False, -1
            if node.val in (target1, target2):
                return True, 1

            left, left_level = traverse(node.left, level + 1)
            right, right_level = traverse(node.right, level + 1)

            if left and right:
                if left_level == 2 and right_level == 2:
                    self.are_cousins = True
                    self.parent = node.val
                return True, left_level + 1
            if left ^ right:
                cur_level = right_level + 1 if left_level == -1 else left_level + 1
                return True, cur_level
            return False, -1

        traverse(self.root, 0)
        print(self.are_cousins)


class TreeCousinsFinder():
    def __init__(self, root):
        self.root = root
        self.grandparent = None
        self.direction = None
        self.parent = None
        self.direction = None
        self.cousins = []

    def traverse(self, node, level):
        if not node:
            return 0, None
        if node.val == self.target:
            return 1, node.val
        left, left_val = self.traverse(node.left, level + 1)
        right, right_val = self.traverse(node.right, level + 1)
        # print('node.val: {} left.val: {} right.val: {} left: {}, right: {}'.format(node.val, left_val, right_val, left, right))

        if left > 0 or right > 0:
            if left == 2 or right == 2:
                self.grandparent = node
                self.direction = 'left' if left == 2 else 'right'
            if left == 1 or right == 1:
                self.parent = node.val
            return 1 + max(left, right), left_val or right_val
        return 0, None

    def locate_cousins(self, node):
        if node:
            parent = node.left if self.direction == 'right' else node.right
        else:
            return []
        if parent is None:
            return self.cousins
        self.cousins.append(parent.left.val) if parent.left is not None else None
        self.cousins.append(parent.right.val) if parent.right is not None else None
        return self.cousins

    def find_cousins(self, target):
        self.target = target
        self.traverse(root, 0)
        print('target: {} \t \nself.parent: {}'.format(target, self.parent))
        # print('self.grandparent.val: {}'.format(self.grandparent.val))
        self.locate_cousins(self.grandparent)
        print(self.cousins)


def sum_tree(root):
    def traverse(node):
        if not node:
            return [0]
        left = traverse(node.left)
        right = traverse(node.right)

        sum_left = sum(left)
        sum_right = sum(right)

        if sum_left + sum_right != 0:
            node.val = sum_left + sum_right
        return [sum_left, sum_right, node.val]

    def print_tree(node):
        if not node:
            return
        print(node.val)
        print_tree(node.left)
        print_tree(node.right)

    print('old tree:')
    print_tree(root)
    print('new tree:')
    traverse(root)
    print_tree(root)


if __name__ == '__main__':
    'https://medium.com/@codingfreak/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f'

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)

    print('spiral_tree:')
    spiral_tree(root)
    print('')

    print('reverse_order_tree:')
    reverse_order_tree(root)
    print('')

    print('reverse_order_tree_iterative:')
    reverse_order_tree_iterative(root)
    print('')

    print('specific_order_print_node:')
    specific_order_print_node(root)
    print('')


    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)

    print('left_view_tree:')
    left_view_tree(root)
    print('')

    print('right_view_tree:')
    right_view_tree(root)
    print('')

    print('top_view_tree: ')
    top_view_tree(root)
    print('')

    print('bottom_view_tree: ')
    bottom_view_tree(root)
    print('')

    print('find_next_node_to_right:')
    print('current_node: {}, neightbor: {}'.format(1, find_next_node_to_right(root, 1)))
    print('current_node: {}, neightbor: {}'.format(2, find_next_node_to_right(root, 2)))
    print('current_node: {}, neightbor: {}'.format(3, find_next_node_to_right(root, 3)))
    print('current_node: {}, neightbor: {}'.format(4, find_next_node_to_right(root, 4)))
    print('current_node: {}, neightbor: {}'.format(5, find_next_node_to_right(root, 5)))
    print('current_node: {}, neightbor: {}'.format(6, find_next_node_to_right(root, 6)))
    print('current_node: {}, neightbor: {}'.format(7, find_next_node_to_right(root, 7)))
    print('current_node: {}, neightbor: {}'.format(8, find_next_node_to_right(root, 8)))
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    # root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print('is_complete_tree: ')
    print(is_complete_tree(root))
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)

    print('check_nodes_are_cousins: ')
    cousin_checker = TreeCousinChecker(root)
    cousin_checker.check_nodes_are_cousins(5, 7)
    print('')
    cousin_checker = TreeCousinChecker(root)
    cousin_checker.check_nodes_are_cousins(8, 11)
    print('')

    print('find_cousins: ')
    cousin_finder = TreeCousinsFinder(root)
    cousin_finder.find_cousins(14)
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print('sum_tree: ')
    sum_tree(root)