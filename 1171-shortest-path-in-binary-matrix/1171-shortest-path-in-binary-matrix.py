class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1

        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        n = len(grid)

        if n == 1: return 1
        
        # queue contains (row, column, distance) tuple
        q = collections.deque()
        q.append((0, 0, 1))

        while q:
            for _ in range(len(q)):
                r, c, dist = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    new_dist = dist + 1

                    if min(nr, nc) < 0 or nr == n or nc == n or grid[nr][nc] == 1:
                        continue
                    
                    if nr == n - 1 and nc == n - 1:
                        return new_dist
                    
                    grid[nr][nc] = 1
                    q.append((nr, nc, new_dist))
        
        return -1