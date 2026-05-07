# ============================================================
# GRAPHS
# ============================================================
# When to use:
#   - problem has nodes + connections (edges)
#   - grid problems — treat each cell as a node
#   - "number of islands", "connected components", "shortest path"
#   - anything with dependencies or relationships
#
# BFS → shortest path, minimum steps
# DFS → explore all paths, connected components, cycle detection


# ── REPRESENTATIONS ─────────────────────────────────────────

# Adjacency list (most common in LeetCode)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
}

# Build from edge list
from collections import defaultdict

def build_graph(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)   # remove for directed graph
    return graph


# ── BFS ON GRAPH ────────────────────────────────────────────
# Use for: shortest path, minimum steps to reach target

from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    steps = 0

    while queue:
        for _ in range(len(queue)):   # process level by level
            node = queue.popleft()
            # do something with node

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        steps += 1

    return steps


# ── DFS ON GRAPH ────────────────────────────────────────────
# Use for: explore all nodes, connected components, cycle detection

def dfs(graph, node, visited):
    visited.add(node)
    # do something with node

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Count connected components
def count_components(n, edges):
    graph = build_graph(n, edges)
    visited = set()
    count = 0

    for node in range(n):
        if node not in visited:
            dfs(graph, node, visited)
            count += 1

    return count


# ── GRID BFS / DFS ──────────────────────────────────────────
# Treat each cell as a node, neighbors are up/down/left/right

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]

def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or grid[r][c] == '0' or (r, c) in visited):
            return
        visited.add((r, c))
        for dr, dc in DIRS:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1

    return count

# BFS shortest path in grid
def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])  # (r, c, steps)
    visited = set([start])

    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == end:
            return steps

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != '#':
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))

    return -1   # no path


# ── TOPOLOGICAL SORT (DAG) ──────────────────────────────────
# Use for: course prerequisites, task scheduling
# Kahn's algorithm (BFS approach)

def topo_sort(n, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * n

    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else []  # empty = cycle exists
