# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        cur = head
        if cur.next == None:
            return head
        
        prev = head
        cur = prev.next
        prev.next = None
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev
        