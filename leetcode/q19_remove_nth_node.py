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
        l1 = ListNode(0)
        l2 = ListNode(0)
        h1 = l1
        l1.next = head
        l2.next = head
        count = -1
        print(l2.val)
        print(l1.val)
        print(h1.val)
        print("onto the loops")
        
        while l2:
            l2 = l2.next
            if l2:
                print(l2.val)
            count += 1
        print("counter at", count)
        print("onto l1")
        
        while l1 and count>n:
            l1=l1.next
            if l1:
                print(l1.val, count, h1.val)
            count-=1
        print("done with l1")
        
        if l1.next:
            l1.next=l1.next.next
            print(l1.val)
            return h1.next
        
        return h1
        