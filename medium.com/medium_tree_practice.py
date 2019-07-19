# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'https://medium.com/@codingfreak/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f'

def print_tree_layers(root):
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
    for layer in node_layers:
        print(layer)


# http://www.techiedelight.com/spiral-order-traversal-binary-tree/
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


# http://www.techiedelight.com/reverse-level-order-traversal-binary-tree/
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


# https://www.techiedelight.com/reverse-level-order-traversal-binary-tree/
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


# http://www.techiedelight.com/print-nodes-binary-tree-specific-order/
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


# http://www.techiedelight.com/print-left-view-of-binary-tree/
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


# http://www.techiedelight.com/print-right-view-binary-tree/
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


# http://www.techiedelight.com/print-top-view-binary-tree/
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


# http://www.techiedelight.com/print-bottom-view-of-binary-tree/
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



# http://www.techiedelight.com/find-next-node-in-same-level-binary-tree/
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


# http://www.techiedelight.com/check-given-binary-tree-complete-binary-tree-not/
def is_complete_tree(root):
    if not root:
        return True
    # print(root.left.val if root.left else None, root.right.val if root.right else None)
    if not root.left and root.right:
        return False
    return is_complete_tree(root.left) and is_complete_tree(root.right)
    

# http://www.techiedelight.com/determine-two-nodes-are-cousins/
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


# http://www.techiedelight.com/print-cousins-of-given-node-binary-tree/
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
        self.traverse(self.root, 0)
        print('target: {} \t \nself.parent: {}'.format(target, self.parent))
        # print('self.grandparent.val: {}'.format(self.grandparent.val))
        self.locate_cousins(self.grandparent)
        print(self.cousins)


# http://www.techiedelight.com/inplace-convert-a-tree-sum-tree/
def sum_tree(root):
    def traverse(node):
        if not node:
            return 0
        left = traverse(node.left)
        right = traverse(node.right)

        if left + right != 0:
            node.val = left + right
        return left + right + node.val

    print('old tree:')
    print_tree_layers(root)
    print('new tree:')
    traverse(root)
    print_tree_layers(root)


# http://www.techiedelight.com/check-given-binary-tree-sum-tree-not/
class CheckSumTree():
    def __init__(self, root):
        self.root = root
        self.is_sum_tree = True

    def traverse(self, node):
        if not node:
            return [0]
        left = self.traverse(node.left)
        right = self.traverse(node.right)

        sum_left = sum(left)
        sum_right = sum(right)

        # print(node.val, sum_left, sum_right, sum_right + sum_left)
        if sum_left != 0 and sum_right != 0:
            if node.val != sum_left + sum_right:
                self.is_sum_tree = False
        return [sum_left, sum_right, node.val]

    def check_sum_tree(self):
        self.traverse(self.root)


# http://www.techiedelight.com/combinations-of-words-formed-replacing-given-numbers-corresponding-english-alphabet/
class WordNumberCombination():
    def __init__(self):
        self.root = None
        self.combinations = []
        self.digit_mapper = 'ABCDEFGHIJKLMNOPQRSTUVWXVZ'

    def word_digit_combination(self, ls):
        import copy
        ls = [str(i) for i in ls]

        def traverse(ls, res):
            # ls - remaining digits     res - results that we add to
            if len(ls) == 0:
                self.combinations.append(res)
                return 
            head = str(ls.pop(0))

            # case 2: adding onto res's last value
            print(head, ls, res + [head])
            traverse(ls, res + [head])

        print('', ls, [])
        first_val = str(ls.pop(0))
        print(first_val, ls, [first_val])
        traverse(ls, [first_val])
        print('')
        
        print(self.combinations)


# http://www.techiedelight.com/determine-given-binary-tree-is-subtree-of-another-binary-tree-not/
class SubtreeChecker():
    def __init__(self, root):
        self.root = root
        self.subtree_root = None
        self.starting_point = None

    def find_starting_point(self, node):
        if not node:
            return
        if node.val == self.subtree_root.val:
            self.starting_point = node
            return
        self.find_starting_point(node.left)
        self.find_starting_point(node.right)

    def compare_trees(self, main_tree_node, sub_tree_node):
        if not main_tree_node and not sub_tree_node:
            return True
        if not sub_tree_node:
            return False
        if not main_tree_node:
            return False
        if sub_tree_node.val != main_tree_node.val:
            return False
        return self.compare_trees(main_tree_node.left, sub_tree_node.left) and self.compare_trees(main_tree_node.right, sub_tree_node.right)

    def sub_tree_checker(self, subtree_root):
        # root is the "subtree"
        self.subtree_root = subtree_root
        self.find_starting_point(self.root)
        is_sum_tree = self.compare_trees(self.starting_point, self.subtree_root)
        print(is_sum_tree)


# http://www.techiedelight.com/find-diameter-of-a-binary-tree/
class DiameterOfTree():
    def __init__(self):
        self.diameter = 0

    def traverse(self, node):
        if not node:
            return 0

        left = self.traverse(node.left)
        right = self.traverse(node.right)
        # print(node.val, max(left, right) + 1)

        if left + right > self.diameter:
            self.diameter = left + right + 1
        return max(left, right) + 1

    def diameter_finder(self, root):
        self.traverse(root)
        print(self.diameter)


# http://www.techiedelight.com/check-given-binary-tree-symmetric-structure-not/
def tree_symmetric(root):
    def traverse(left, right):
        if not left and not right:
            return True
        if (left is not None)  ^ (right is not None):
            return False
        return traverse(left.left, right.right) and traverse(left.right, right.left)

    is_symmetric = traverse(root.left, root.right)
    print(is_symmetric)


# http://www.techiedelight.com/convert-binary-tree-to-its-mirror/
def mirror_binary_tree(node):
    if not node:
        return
    temp = node.left
    node.left = node.right
    node.right = temp
    mirror_binary_tree(node.left)
    mirror_binary_tree(node.right)


# https://www.techiedelight.com/determine-binary-tree-can-converted-another-number-swaps-left-right-child/
def transform_another_tree(n1, n2):
    if not n1 and not n2:
        return True
    'set(TreeNode, None) compare sets of both trees'
    n1_val = n1.val if n1 else None
    n2_val = n2.val if n2 else None
    if n1_val != n2_val:
        return False

    n1_left_val = n1.left.val if n1.left else None
    n1_right_val = n1.right.val if n1.right else None

    n2_left_val = n2.left.val if n2.left else None
    n2_right_val = n2.right.val if n2.right else None

    n1_set = {n1_left_val, n1_right_val}
    n2_set = {n2_left_val, n2_right_val}
    print({n1_val, n2_val}, n1_set, n2_set, n1_set == n2_set)

    if n1_set != n2_set:
        return False

    if n1_left_val == n2_left_val and n1_right_val == n2_right_val:
        return transform_another_tree(n1.left, n2.left) and transform_another_tree(n1.right, n2.right)
    elif n1_left_val == n2_right_val and n1_right_val == n2_left_val:
        return transform_another_tree(n1.right, n2.left) and transform_another_tree(n1.left, n2.right)
    return False


# https://www.techiedelight.com/find-lowest-common-ancestor-lca-two-nodes-binary-tree/
class LowestCommonAncestor():
    def __init__(self, root):
        self.root = root
        self.lowest_common_ancestor = None
        self.n1 = None
        self.n2 = None

    def traverse(self, node):
        if not node:
            return False
        if node.val in (self.n1, self.n2):
            self.lowest_common_ancestor = node.val
            return True

        left = self.traverse(node.left)
        right = self.traverse(node.right)

        if left and right:
            self.lowest_common_ancestor = node.val
            return True
        if left ^ right:
            return True

        return False

    def find_lowest_common_ancestor(self, n1, n2):
        self.lowest_common_ancestor = None
        self.n1 = n1
        self.n2 = n2
        self.traverse(self.root)
        print('n1: {} \t n2: {} \t lowest_common_ancestor: {}'.format(n1, n2, self.lowest_common_ancestor))


# http://www.techiedelight.com/print-all-paths-from-root-to-leaf-nodes-binary-tree/
def print_all_paths_from_root_to_leaf(root):
    def traverse(node, path):
        if not node:
            return

        if node.left is None and node.right is None:
            updated_path = path + [node.val]
            print(' -> '.join(str(i) for i in updated_path))
            return
        elif node.left is None and node.right is not None:
            traverse(node.right, path + [node.val])
        elif node.left is not None and node.right is None:
            traverse(node.left, path + [node.val])
        else:
            traverse(node.left, path + [node.val])
            traverse(node.right, path + [node.val])
    traverse(root, [])


# http://www.techiedelight.com/find-vertical-sum-given-binary-tree/
def vertical_sum_tree(root):
    sums = {}
    def traverse(node, axis):
        if not node:
            return
        if axis not in sums.keys():
            sums[axis] = node.val
        else:
            sums[axis] += node.val
        traverse(node.left, axis - 1)
        traverse(node.right, axis + 1)
    traverse(root, 0)
    print(sums)


# https://www.techiedelight.com/find-ancestors-of-given-node-binary-tree/
class AncestorsOfNode():    
    def traverse(self, node, target):
        if not node:
            return []
        if node.val == target:
            return [node.val]
        left_ls = self.traverse(node.left, target)
        right_ls = self.traverse(node.right, target)

        if len(left_ls) > 0:
            return [node.val] + left_ls
        if len(right_ls) > 0:
            return [node.val] + right_ls
        return []

    def ancestor_finder(self, root, target):
        ancestor_path = self.traverse(root, target)
        print(target, ancestor_path)


# http://www.techiedelight.com/vertical-traversal-binary-tree/
def get_vertical_paths(root):
    vertical_paths = {}
    def traverse(node, axis):
        if not node:
            return
        if axis not in vertical_paths.keys():
            vertical_paths[axis] = [node.val]
        else:
            vertical_paths[axis].append(node.val)
        traverse(node.left, axis - 1)
        traverse(node.right, axis + 1)
    traverse(root, 0)
    
    for path in sorted(vertical_paths.keys()):
        print(vertical_paths[path])


# https://www.techiedelight.com/distance-between-given-pairs-of-nodes-binary-tree/
class DistanceBetweenNodes():
    def __init__(self):
        self.distance = 0

    def traverse(self, node, n1, n2):
        if not node:
            return 0
        if node.val in (n1, n2):
            return 1

        left = self.traverse(node.left, n1, n2)
        right = self.traverse(node.right, n1, n2)

        if left > 0 and right > 0:
            self.distance = left + right
            return left + right
        if left > 0 or right > 0:
            return max(left, right) + 1
        return 0

    def find_distance(self, root, n1, n2):
        self.distance = 0
        self.traverse(root, n1, n2)
        print(n1, n2, 'distance: {}'.format(self.distance))


# https://www.techiedelight.com/find-diagonal-sum-given-binary-tree/
class DiagonalSums():
    def __init__(self):
        self.diagonal_sums = {}

    def traverse(self, node, x_axis, y_axis):
        if not node:
            return
        diag_idx = abs(x_axis - y_axis)
        if diag_idx not in self.diagonal_sums.keys():
            self.diagonal_sums[diag_idx] = node.val
        else:
            self.diagonal_sums[diag_idx] += node.val

        self.traverse(node.left, x_axis - 1, y_axis + 1)
        self.traverse(node.right, x_axis + 1, y_axis + 1)

    def get_diagonal_sums(self, root):
        self.diagonal_sums = {}
        self.traverse(root, 0, 0)
        print(self.diagonal_sums)


# http://www.techiedelight.com/print-diagonal-traversal-binary-tree/
class DiagonalTraversal():
    def __init__(self):
        self.diagonal_paths = {}

    def traverse(self, node, x_axis, y_axis):
        if not node:
            return
        diag_idx = abs(x_axis - y_axis)
        if diag_idx not in self.diagonal_paths.keys():
            self.diagonal_paths[diag_idx] = [node.val]
        else:
            self.diagonal_paths[diag_idx].append(node.val)

        self.traverse(node.left, x_axis - 1, y_axis + 1)
        self.traverse(node.right, x_axis + 1, y_axis + 1)

    def get_diagonal_paths(self, root):
        self.diagonal_paths = {}
        self.traverse(root, 0, 0)
        for key in self.diagonal_paths.keys():
            print(self.diagonal_paths[key])


# https://www.techiedelight.com/print-corner-nodes-every-level-binary-tree/
def print_corner_trees(root):
    cur_level = [root]
    next_level = []

    print(root.val)
    while len(cur_level) > 0 or len(next_level) > 0:
        while len(cur_level) > 0:
            node = cur_level.pop(0)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        cur_level = next_level
        next_level = []
        
        if len(cur_level) == 0:
            pass
        elif len(cur_level) == 1:
            print(cur_level.val)
        else:
            head = cur_level[0]
            tail = cur_level[-1]
            print(head.val, tail.val)


# Node of a doubly linked list  
class DllNode: 
    # def __init__(self, next=None, prev=None, data=None):
    def __init__(self, val):
        self.val = val
        self.next = None # reference to next node in DLL 
        self.prev = None # reference to previous node in DLL 

class TreeToDoubleLinkedList():
    def __init__(self):
        self.ls = []
        self.linked_list_head = None

    # in-order traversal
    def traverse(self, node):
        if not node:
            return
        self.traverse(node.left)
        node_val = node.val
        self.ls.append(DllNode(node_val))
        self.traverse(node.right)

    def create_double_linked_list(self):
        self.linked_list_head = self.ls[0]
        length = len(self.ls)
        for i in range(1, length):
            node = self.ls[i]
            prev_node = self.ls[i - 1]
            prev_node.next = node
            node.prev = prev_node

    def print_doubly_linked_list(self):
        n = self.linked_list_head
        while n:
            print('cur', n.val, 'prev', n.prev.val if n.prev else None, 'next', n.next.val if n.next else None)
            n = n.next

    def tree_to_doubly_linked_list(self, root):
        self.ls = []
        self.traverse(root)
        self.create_double_linked_list()
        self.print_doubly_linked_list()
