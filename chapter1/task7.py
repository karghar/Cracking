#set all elements to 0


class Solution(object):
	def matrixZeroing(self, matrix):
		rowsZero = [1] * len(matrix)
		columnsZero = [1] * len(matrix)

		for row in range(0, len(matrix)):
			for col in range(0, len(matrix)):
				if matrix[row][col] == 0:
					rowsZero[row] = 0
					columnsZero[col] = 0


		for row in range(0, len(matrix)):
			for col in range(0, len(matrix)):
				if rowsZero[row] == 0 or columnsZero[col] == 0:
					matrix[row][col] = 0

		return matrix

