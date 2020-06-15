# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insert(self, root, item): 
        temp = ListNode(item) 
          
        if (root == None): 
            root = temp 
        else : 
            ptr = root 
            while (ptr.next != None): 
                ptr = ptr.next
            ptr.next = temp 
          
        return root 

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_digit = 0 # this is the sum of the current digit
        remainder = 0
        started = False

        ans = None

        while l1 is not None or l2 is not None:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            sum_digit = l1_val + l2_val + remainder
            
            if sum_digit > 9:
                sum_digit = sum_digit % 10
                remainder = 1
            else:
                remainder = 0
            # print(sum_digit)

            ans = self.insert(ans, sum_digit)

            # this handles if one linked list is exhausted
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if remainder > 0:
            self.insert(ans, remainder)
            print(remainder)

        return ans


if __name__ == '__main__':
    num1 = ListNode(2)
    num1.next = ListNode(4)
    num1.next.next = ListNode(3)

    num2 = ListNode(5)
    num2.next = ListNode(6)
    num2.next.next = ListNode(4)

    s = Solution()
    ans = s.addTwoNumbers(num1, num2)
    while ans is not None:
        print(ans.val)
        ans = ans.next
    print("")

    num1 = ListNode(9)
    num1.next = ListNode(9)
    num1.next.next = ListNode(9)
    num1.next.next.next = ListNode(3)

    num2 = ListNode(9)
    num2.next = ListNode(9)
    num2.next.next = ListNode(9)
    num2.next.next.next = ListNode(9)

    s = Solution()
    ans = s.addTwoNumbers(num1, num2)
    while ans is not None:
        print(ans.val)
        ans = ans.next
