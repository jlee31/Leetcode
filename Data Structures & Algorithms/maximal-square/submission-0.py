class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # top down approach
        # memoization

        numRows = len(matrix)
        numCols = len(matrix[0])
        cache = {} # stores key as (r,c) and value as lenSquare that it can create

        def memo(r,c):
            if r >= numRows or c >= numCols:
                cache[(r,c)] = 0
            if (r,c) not in cache:
                down = memo(r+1, c)
                left = memo(r, c+1)
                diag = memo(r+1, c+1)

                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down,left,diag)
            
            return cache[(r,c)]
        
        memo(0,0)

        return max(cache.values()) ** 2
                

