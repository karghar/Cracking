# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def isPalindrome(self, list):
		first = list
		middle, last = list, list
		while last.next:
			if last.next.next:
				last = last.next.next
			middle = middle.next

		while middle:
			if first.val != middle.val:
				return False
			first, middle = first.next, middle.next

		return True