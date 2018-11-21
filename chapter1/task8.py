
class Solution(object):
	def stringisSubstring(self, s1, s2):
		if len(s1) != len(s2):
			return False
		for i in range(0, len(s1)):
			if s2[i:] + s2[:i] == s1:
				return True

		return False
