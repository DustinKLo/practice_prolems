# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        m = 0
        ahead = head
        while ahead.next != None:
            print(ahead.val)
            ahead = ahead.next
            m += 1
        print(ahead.val)
        
        print('onto the next part index: {}'.format(m-n))
        print(head.val)
        
        i = 1
        while head.next:
            if i == m-n:
                head = head.next.next
                print(head.val)
            else:
                head = head.next
                print(head.val)
            i += 1
        
        return head