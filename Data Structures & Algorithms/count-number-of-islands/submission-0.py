from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r,c))
            while q:
                row, col = q.popleft() # if u do pop, its a dfs
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r, c)
                    visited.add((r,c))
                    count +=1
        return count