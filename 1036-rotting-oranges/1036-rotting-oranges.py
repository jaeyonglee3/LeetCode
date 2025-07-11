class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-source BFS, where the sources are the rotten oranges
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        num_fresh = 0
        num_minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    num_fresh += 1
        
        while q and num_fresh > 0:
            num_minutes += 1
            
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIRS:
                    new_r, new_c = r + dr, c + dc

                    if min(new_r, new_c) < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] != 1:
                        continue

                    # turn it rotten and add to queue for further processing
                    num_fresh -= 1
                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c))
        
        return num_minutes if num_fresh == 0 else -1
                