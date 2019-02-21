# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# find mid point
# reverse second half of the linked list
# loop from beginning:
#   beginning value = mid point value
#   beginnig value -> next and mid point value -> next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        
        slow = head
        fast = head
        while fast != None and fast.next != None:
            if fast.next.next is not None:
                slow = slow.next
            fast = fast.next.next
        
        mid_anchor = slow
        mid = mid_anchor.next
        
        prev = mid
        cur = mid.next
        prev.next = None
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        mid_anchor.next = prev
        cur = head
        slow = slow.next
        while cur != None and slow != None:
            if cur.val != slow.val:
                return False
            cur = cur.next
            slow = slow.next
            
        return True