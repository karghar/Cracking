# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def deleteMiddle(self, node):
		if not node or not node.next:
			return node
		node.val = node.next.val
		nodeNext = node.next
		node.next = None, node.next.next
		#garbage collections
		nodeNext.next = None




