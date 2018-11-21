# unique characters
from collections import Counter, defaultdict


class Solution(object):
	def uniqueCharacters(self, string):
		if not string:
			return True
		counter = Counter(string)
		for (letter, repetition) in counter.most_common():
			if repetition != 1:
				return False
			else:
				return True
		return True

	def uniqueCharactersHashMap(self, string):
		if not string:
			return True
		charDict = defaultdict(int)
		for char in defaultdict:
			if defaultdict[char] != 0:
				return False
			defaultdict[char] += 1

		return True

	def uniqueCharactersNoStructure(self, string):
		checker = 0
		for chr in string:
			value = ord(chr) - ord('a')
			if (checker & (1 << value)) > 0:
				return False
			else:
				checker |= (1 << value)

		return True

