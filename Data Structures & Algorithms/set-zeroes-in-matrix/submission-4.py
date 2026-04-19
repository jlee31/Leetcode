class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # goal: solution in o(1) space
        # idea: make the first row and first col 0s or 1s

        row_zero = False
        col_zero = False

        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                row_zero = True
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_zero = True

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
                
        for row in range(1,len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][0] == 0:
                    matrix[row][col] = 0
                if matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if row_zero:
            matrix[0] = [0] * len(matrix[0])
        if col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

