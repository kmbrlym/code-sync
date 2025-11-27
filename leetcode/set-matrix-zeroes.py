class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        set_row_zeros = False
        set_column_zeros = False
        for i in matrix[0]:
            if i == 0:
                set_row_zeros = True
        for i in matrix:
            if i[0] == 0:
                set_column_zeros = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[i])
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0
        if set_row_zeros:
            matrix[0] = [0] * len(matrix[0])
        if set_column_zeros:
            for j in range(len(matrix)):
                matrix[j][0] = 0