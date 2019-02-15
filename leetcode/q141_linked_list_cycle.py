# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if head.next == None:
            return False
        if head.next.next == None:
            return False
        
        slow = head
        fast = head
        while slow.next != None or fast.next != None:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            # print(slow.val, fast.val)
            if fast == None or slow.next == None:
                return False
            if slow == fast:
                return True
                