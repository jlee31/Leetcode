class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        cache = {} #(r,c) = numWays
        # dp(r,c) = dp(r+1,c) + dp(r,c+1
        def memo(r,c):
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if (r,c) not in cache:
                down = memo(r+1, c)
                left = memo(r, c+1)

                cache[(r,c)] = down + left
            
            return cache[(r,c)]

        memo(0,0)
        # print(cache)
        return cache[(0,0)]