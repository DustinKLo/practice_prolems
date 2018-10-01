# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = l3 = ListNode(0)
        
        while l1 and l2: # and instead of or to avois breaking, leaves last value open in l1 or l2
            
            if l1.val < l2.val:
                print("l1 ({}) < l2 ({})".format(l1.val, l2.val))
                # l3's next val is l1's current value
                # shift l1's value to next
                l3.next, l1 = l1, l1.next
                
            else:
                print("l2 ({}) <= l1 ({})".format(l2.val, l1.val))
                l3.next, l2 = l2, l2.next
            
            l3 = l3.next # shift l3's value to next
        
        
        l3.next = l1 or l2
        
        if l1:
            print("last value: l1 {}".format(l1.val))
        if l2:
            print("last value: l2 {}".format(l2.val))
        return ans.next
        