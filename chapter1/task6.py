#matrix rotation


class Solution(object):
	def matrixNinetyDegree(self, matrix):
		result = []
		matrixLen = len(matrix)
		for x in range(0, matrixLen):
			innerRow = []
			for y in range(matrixLen - 1, -1, -1):
				innerRow.append(matrix[x][y])

			result.append(innerRow)

		return result

