# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def kthToLast(self, node, k):
		pointer, pointerAhead = node, node
		for x in range(k):
			pointerAhead = pointerAhead.next

		while pointerAhead.next:
			pointer = pointer.next
			pointerAhead = pointerAhead.next

		return pointerAhead


