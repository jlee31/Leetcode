class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if j > i:
                    a = matrix[i][j]
                    b = matrix[j][i]
                    matrix[i][j] = b
                    matrix[j][i] = a

        for i in range(n):
            matrix[i] = [matrix[i][j] for j in range(n-1, -1, -1)]

        return