# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def print_linked_list(head):
        while head is not None:
            print(head.val)
            head = head.next

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        
        ls = []
        while head is not None:
            ls.append(head.val)
            head = head.next

        ls_len = len(ls)

        # find the mod, k % len(ls) (minimum rotations)
        k_mod = k % ls_len
        print(ls)
        print("k: %d" % k)
        ls = ls[ls_len - k_mod:] + ls[:ls_len - k_mod]
        print(ls)
        print("############################\n")

        ans = new_head = ListNode(0)
        for n in ls:
            new_head.next = ListNode(n)
            new_head = new_head.next
        return ans.next


if __name__ == '__main__':
    s = Solution()

    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    ans = s.rotateRight(root, 2)

    ans = s.rotateRight(root, 1)
