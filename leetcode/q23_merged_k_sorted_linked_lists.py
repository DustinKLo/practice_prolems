from Queue import PriorityQueue

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

"""
[
  1->4->5,
  1->3->4,
  2->6
]
"""

class Solution(object):
	# def __init__(self):
	#	 self.priority_queue = []
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		# THIS WAS WHAT I WAS LOOKING FOR
		# NOT HHAVING TO MANUALLY PUSH A NEW NODE TO THEH TAIL, O(N)
		head = pt = ListNode()
		
		q = PriorityQueue()
		for ll in lists:
			cur = ll
			while cur is not None:
				q.put(cur.val)
				cur = cur.next

		while not q.empty():
			i = q.get()
			pt.next = ListNode(i)
			pt = pt.next
		return head.next


if __name__ == '__main__':
	root1 = ListNode(1)
	root1.next = ListNode(4)
	root1.next.next = ListNode(5)

	root2 = ListNode(1)
	root2.next = ListNode(3)
	root2.next.next = ListNode(4)

	root3 = ListNode(2)
	root3.next = ListNode(6)

	s = Solution()
	ans = s.mergeKLists([root1, root2, root3])
	while ans is not None:
		print(ans, ans.val)
		ans = ans.next


