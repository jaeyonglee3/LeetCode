class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque()
        res = 0

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    grid[r][c] = - 1
                    q.append((r, c))
        
        # If there are no land or no water, return -1
        if not q or len(q) == N * N:
            return -1
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr == N or nc == N or grid[nr][nc] != 0:
                        continue
                    
                    if grid[r][c] == - 1:
                        grid[nr][nc] = 1
                    else:
                        grid[nr][nc] = grid[r][c] + 1

                    res = grid[nr][nc]
                    q.append((nr, nc))
        
        return res