# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        while head != None:
            if head.val == val:
                head = head.next
            else:
                break
            
        cur = head
        while cur != None and cur.next != None:
            # print(cur.val)
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
        