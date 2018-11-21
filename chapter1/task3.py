# unique characters
from collections import Counter, defaultdict


class Solution(object):
	#using sets
	def isPermutation(self, lhsStr, rhsStr):
		if not lhsStr and rhsStr:
			return False
		if not rhsStr and lhsStr:
			return False
		lhsSet = set(lhsStr)
		rhsSet = set(rhsStr)
		return lhsSet.issubset(rhsSet) and lhsSet.issuperset(rhsSet)

