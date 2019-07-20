from medium_tree_practice import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

    print('1. spiral_tree:')
    spiral_tree(root)
    print('')

    print('2. reverse_order_tree:')
    reverse_order_tree(root)
    print('')

    print('3. reverse_order_tree_iterative:')
    reverse_order_tree_iterative(root)
    print('')

    print('4. specific_order_print_node:')
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

    print('5. left_view_tree:')
    left_view_tree(root)
    print('')

    print('6. right_view_tree:')
    right_view_tree(root)
    print('')

    print('7. top_view_tree: ')
    top_view_tree(root)
    print('')

    print('8. bottom_view_tree: ')
    bottom_view_tree(root)
    print('')

    print('9. find_next_node_to_right:')
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
    print('10. is_complete_tree: ')
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

    print('11. check_nodes_are_cousins: ')
    cousin_checker = TreeCousinChecker(root)
    cousin_checker.check_nodes_are_cousins(5, 7)
    print('')
    cousin_checker = TreeCousinChecker(root)
    cousin_checker.check_nodes_are_cousins(8, 11)
    print('')

    print('12. find_cousins: ')
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

    print('13. sum_tree: ')
    sum_tree(root)
    print('')

    print('14. sum_tree_checker.is_sum_tree: ')
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

    print('15. sum_tree_checker.is_sum_tree: ')
    sum_tree_checker = CheckSumTree(root)
    sum_tree_checker.check_sum_tree()
    print(sum_tree_checker.is_sum_tree)
    print('')

    print('16. WordNumberCombination: ')
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
    # root.right.right.left = TreeNode(8)

    subtree = TreeNode(3)
    subtree.left = TreeNode(6)
    subtree.right = TreeNode(7)
    print('17. SubtreeChecker')
    subtree_checker = SubtreeChecker(root)
    subtree_checker.sub_tree_checker(subtree)
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right = TreeNode(7)
    root.right.right = TreeNode(8)
    root.right.right.right = TreeNode(9)
    root.right.right.right.left = TreeNode(10)
    root.right.right.right.left.left = TreeNode(11)
    root.right.right.right.right = TreeNode(12)
    print('18. DiameterOfTree')
    # print_tree_layers(root)
    diameter_tree_obj = DiameterOfTree()
    diameter_tree_obj.diameter_finder(root)

    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.left.left = TreeNode(0)
    root.left.left.right = TreeNode(0)
    root.left.left.right.left = TreeNode(0)
    root.left.left.right.left.right = TreeNode(0)
    root.left.right = TreeNode(0)
    root.left.right.right = TreeNode(0)
    root.left.right.right.left = TreeNode(0)
    root.left.right.right.right = TreeNode(0)
    root.left.right.right.right.left = TreeNode(0)
    root.right = TreeNode(0)
    diameter_tree_obj = DiameterOfTree()
    diameter_tree_obj.diameter_finder(root)

    print('19. tree_symmetric')
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    tree_symmetric(root)
    print('')

    print('20. mirror_binary_tree')
    print_tree_layers(root)
    mirror_binary_tree(root)
    print_tree_layers(root)
    print('')

    print('21. transform_another_tree')
    r1 = TreeNode(6)
    r1.left = TreeNode(3)
    r1.right = TreeNode(8)
    r1.left.left = TreeNode(1)
    r1.left.right = TreeNode(7)
    r1.right.left = TreeNode(4)
    r1.right.right = TreeNode(2)
    r1.right.left.left = TreeNode(7)
    r1.right.left.right = TreeNode(1)
    r1.right.right.right = TreeNode(3)

    r2 = TreeNode(6)
    r2.left = TreeNode(8)
    r2.right = TreeNode(3)
    r2.left.left = TreeNode(2)
    r2.left.right = TreeNode(4)
    r2.right.left = TreeNode(7)
    r2.right.right = TreeNode(1)
    r2.left.left.left = TreeNode(3)
    r2.left.right.left = TreeNode(1)
    r2.left.right.right = TreeNode(7)
    print(transform_another_tree(r1, r2))
    print('')

    print('22. LowestCommonAncestor')
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(8)
    root.right.right.right = TreeNode(9)
    lowest_common_ancestor = LowestCommonAncestor(root)
    lowest_common_ancestor.find_lowest_common_ancestor(6, 7)
    lowest_common_ancestor.find_lowest_common_ancestor(5, 8)
    lowest_common_ancestor.find_lowest_common_ancestor(3, 6)
    lowest_common_ancestor.find_lowest_common_ancestor(2, 5)
    print('')

    print('23. print_all_paths_from_root_to_leaf')
    print_all_paths_from_root_to_leaf(root)
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)

    print('24. vertical_sum_tree')
    vertical_sum_tree(root)
    print('')

    print('25. get_vertical_paths')
    get_vertical_paths(root)
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(8)
    root.right.right.right = TreeNode(9)
    print('26. ancestors_of_node')
    ancestor_finder_obj = AncestorsOfNode()
    ancestor_finder_obj.ancestor_finder(root, 8)
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    print('27. DistanceBetweenNodes')
    distance_between_nodes = DistanceBetweenNodes()
    distance_between_nodes.find_distance(root, 7, 6)
    distance_between_nodes.find_distance(root, 8, 4)
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    print('28. DiagonalSums')
    diagonal_sums_obj = DiagonalSums()
    diagonal_sums_obj.get_diagonal_sums(root)
    print('')

    print('29. DiagonalTraversal')
    diagonal_sums_obj = DiagonalTraversal()
    diagonal_sums_obj.get_diagonal_paths(root)
    print('')

    root = TreeNode(6)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(2)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(7)
    root.right.right.right = TreeNode(3)
    print('30. print_corner_trees')
    print_corner_trees(root)
    print('')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print('31. TreeToDoubleLinkedList')
    tree_to_double_linked_list_obj = TreeToDoubleLinkedList()
    tree_to_double_linked_list_obj.tree_to_doubly_linked_list(root)
    print('')

    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(7)
    print('32. RemoveHalfNodes')
    remove_half_nodes = RemoveHalfNodes(root)
    print_tree_layers(remove_half_nodes.root)
    print('')
    remove_half_nodes.remove_half_nodes()
    print_tree_layers(remove_half_nodes.root)
    print('')

    root = TreeNode(6)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(2)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(7)
    root.right.right.right = TreeNode(10)
    print('33. RemoveNodesSumPathK')
    remove_nodes_sum_path_k_obj =  RemoveNodesSumPathK(root)
    print('before')
    print_all_paths_from_root_to_leaf(remove_nodes_sum_path_k_obj.root)
    remove_nodes_sum_path_k_obj.remove_nodes(20)
    print('\nafter')
    print_all_paths_from_root_to_leaf(remove_nodes_sum_path_k_obj.root)
    print('')

    print('34. MaximumSumPath')
    max_sum_path = MaximumSumPath()
    max_sum_path.find_max_path(root)
    print('')
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    print('35. checked_balanced_tree')
    checked_balanced_tree = HeightBalancedTree()
    checked_balanced_tree.is_balanced_tree(root)
