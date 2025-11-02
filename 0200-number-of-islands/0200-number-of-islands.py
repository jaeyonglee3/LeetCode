class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS approach: visit every cell. If the cell is an island,
        # we will use BFS to mark it and every connected "1" as "0"
        # so that we don't count that same island twice
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    grid[r][c] = "0"

                    for dr, dc in DIRS:
                        nr, nc = r + dr, c + dc
                        if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == "0":
                            continue
                        q.append((nr, nc))
             
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        
        return res