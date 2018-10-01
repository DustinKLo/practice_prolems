# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l1_ans = l1 = ListNode(0)
        l2_ans = l2 = ListNode(0)
        ans = l3 = ListNode(0)
        
        i = 1
        while head:
            if i % 2 == 0:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
            i += 1
            
        print("onto the next part")

        l1_ans = l1_ans.next
        l2_ans = l2_ans.next
        while l1_ans and l2_ans:
            print("l1: {}".format(l1_ans.val))
            l3.next = l1_ans
            l1_ans = l1_ans.next
            l3 = l3.next
            
            print("l2: {}".format(l2_ans.val))
            l3.next = l2_ans
            l2_ans = l2_ans.next
            l3 = l3.next
            
        print("2nd part completed")
        return head
