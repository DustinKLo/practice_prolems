# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ans = ListNode(None)
        while len(lists) > 1:
            i = 0
            min_index = None
            min_val = float('inf')
            while i < len(lists):
                if lists[i] is None:
                    lists.pop(i)
                else:
                    if lists[i].val < min_val:
                        min_val = lists[i].val
                        min_index = i
                    i += 1
            lists[min_index] = lists[min_index].next
            print(min_val, min_index)
            # ans.next = 
        
        return None

