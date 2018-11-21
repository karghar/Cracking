


class Solution(object):
	def compressedString(self, seq):
		if not seq:
			return seq
		newStr = ""
		lastChr = seq[0]
		howMany = 0
		for chr in seq:
			if chr == lastChr:
				howMany += 1
			else:
				newStr += lastChr + str(howMany)
				howMany = 1
				lastChr = chr
		newStr += lastChr + str(howMany)

		if len(newStr) < seq:
			return newStr

		return seq
