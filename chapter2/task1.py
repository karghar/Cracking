# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def duplicatedUnsortedLinkList(self, node):
		values = set()
		head = ListNode(0)
		head.next = node
		prev = node

		while node:
			if node.val in values:
				prev.next = node.next
			else:
				values.add(node.val)
			prev = node
			node = node.next

		return head.next

	def duplicateUnsortedNoStructure(self, node):
		head = ListNode(0)
		head.next = node
		prev = node

		while node:
			value = node.val
			nodeAhead = node.next
			prev = node
			while nodeAhead:
				if nodeAhead.val == value:
					prev.next = nodeAhead.next
				prev = nodeAhead
				nodeAhead = nodeAhead.next

		return head.next
