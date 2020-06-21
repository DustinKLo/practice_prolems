# Definition for singly-linked list.
class ListNode(object):
	 def __init__(self, val=0, next=None):
		 self.val = val
		 self.next = next


class Solution(object):
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		cur = head
		vals = []
		while cur is not None:
			vals.append(cur.val)
			cur = cur.next

		# print(vals)
		i = 0
		while i < len(vals):
			if i < len(vals) - 1:
				tmp = vals[i+1]
				vals[i+1] = vals[i]
				vals[i] = tmp
			else:
				pass
			i += 2
		print(vals)

		ans = new_head = ListNode(0)
		for n in vals:
			new_head.next = ListNode(n)
			new_head = new_head.next

		return ans.next

		
if __name__ == '__main__':
	s = Solution()

	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)
	ans = s.swapPairs(head)
