# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def partitionList(self, node, x):
		head = ListNode(0)
		head.next = node
		left, rightStart = head, ListNode(0)
		right = rightStart
		while node:
			if node.val < x:
				left.next = node
				left = left.next
			else:
				right.next = node
				right = right.next
			node = node.next
		if not left:
			return rightStart.next
		left.next = rightStart.next

		return head.next





