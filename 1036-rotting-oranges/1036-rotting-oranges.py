class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        q = collections.deque()
        num_fresh = 0
        total_mins = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while q and num_fresh:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIRS:
                    new_r, new_c = r + dr, c + dc

                    if min(new_r, new_c) < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] != 1:
                        continue
                    
                    grid[new_r][new_c] = 2
                    num_fresh -= 1
                    q.append((new_r, new_c))
                
            total_mins += 1
        
        return total_mins if num_fresh == 0 else -1