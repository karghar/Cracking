# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def addForwardOrder(self, lhsNode, rhsNode):
		head = ListNode(0)
		resultNode = head
		carryOver = 0
		while lhsNode or rhsNode:
			lhsVal, rhsVal = 0, 0
			if lhsNode:
				lhsVal = lhsNode.val
			if rhsNode:
				rhsVal = rhsNode.val
			carryOver, value = divmod(lhsVal + rhsVal + carryOver, 10)
			resultNode.next = ListNode(value)
			resultNode = resultNode.next
			if lhsNode:
				lhsNode = lhsNode.next
			if rhsNode:
				rhsNode = rhsNode.next
		if carryOver > 0:
			resultNode.next = ListNode(carryOver)


		return head.next

	def backwardAddition(self, lhsNode, rhsNode):
		if not lhsNode:
			return 0, rhsNode
		if not rhsNode:
			return 0, lhsNode

		carryOver, node = self.backwardAddition(lhsNode.next, rhsNode.next)

		carryOver, value = divmod(lhsNode.val + rhsNode.val + carryOver, 10)
		resultNode = ListNode(value)
		resultNode.next = node
		return carryOver, resultNode

	def addBackwardOrder(self, lhsNode, rhsNode):
		carryOver, resultNode = self.backwardAddition(lhsNode, rhsNode)
		if carryOver > 0:
			result = ListNode(carryOver)
			result.next = resultNode
			return result

		return resultNode







