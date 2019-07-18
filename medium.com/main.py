from medium_tree_practice import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    print('')

    print('sum_tree_checker.is_sum_tree: ')
    print_tree_layers(root)
    sum_tree_checker = CheckSumTree(root)
    sum_tree_checker.check_sum_tree()
    print(sum_tree_checker.is_sum_tree)
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print_tree_layers(root)

    print('sum_tree_checker.is_sum_tree: ')
    sum_tree_checker = CheckSumTree(root)
    sum_tree_checker.check_sum_tree()
    print(sum_tree_checker.is_sum_tree)
    print('')

    print('WordNumberCombination: ')
    word_digit_combination = WordNumberCombination()
    word_digit_combination.word_digit_combination([1, 2, 2, 1])
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(8)

    subtree = TreeNode(3)
    subtree.left = TreeNode(6)
    subtree.right = TreeNode(7)
    print('SubtreeChecker')
    subtree_checker = SubtreeChecker(root)
    subtree_checker.sub_tree_checker(subtree)
