class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix) * [0]
        n = len(matrix[0]) * [0]
        # first sol ill make a copy and see which parts need to be changed
        # second sol ill try o(1) space

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    m[row] = 1
                    n[col] = 1
                
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if m[row] == 1:
                    matrix[row][col] = 0
                if n[col] == 1:
                    matrix[row][col] = 0
        

                