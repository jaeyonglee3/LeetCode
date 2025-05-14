class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque()
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = - 1
                    q.append((r, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 0:
                        continue
                    
                    if grid[r][c] == - 1:
                        grid[nr][nc] = 1
                    else:
                        grid[nr][nc] = grid[r][c] + 1

                    res = grid[nr][nc]
                    q.append((nr, nc))
        
        return res if res != 0 else -1