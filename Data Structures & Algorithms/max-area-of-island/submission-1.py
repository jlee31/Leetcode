from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            directions = [[1,0], [0,1], [-1, 0], [0, -1]]
            currMax = 1
            q.append((r,c))

            while q:
                row, col = q.pop()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == 1):
                        q.append((r,c))
                        visited.add((r,c))
                        currMax += 1 
            
            return currMax


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currMax = bfs(r,c)
                    if currMax > maxArea:
                        maxArea = currMax
                    visited.add((r,c))
                    

        return maxArea