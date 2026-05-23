from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        spreadTime = 0
        numFresh = 0

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                if grid[r][c] == 1:
                    numFresh += 1
        
        if numFresh == 0:
            return 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        
        while q:
            row,col,time = q.popleft()
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2         
                    numFresh -= 1
                    spreadTime = max(spreadTime, time + 1)
                    q.append((nr, nc, time + 1))

        return spreadTime if numFresh == 0 else -1