class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down
        cache = {}
        def memo(r,c):
            if r >= m or c >= n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            if (r,c) not in cache:
                top = memo(r+1, c)
                left = memo(r, c+1)
                cache[(r,c)] = top + left
            return cache[(r,c)]

        return memo(0,0) 
        