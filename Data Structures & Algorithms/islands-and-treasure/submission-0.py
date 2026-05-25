from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        
        def bfs(q):
            
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            while q:
                nr, nc, dist = q.popleft()
                for dr, dc in directions:
                    r = nr + dr
                    c = nc + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == INF:
                        q.append((r,c, dist+1))
                        grid[r][c] = dist + 1

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        bfs(q)
        return
        
                