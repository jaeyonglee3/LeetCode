class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()  # holds (r, c) positions of rotten oranges only
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh != 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                # Visit all the neighbouring cells and turn any fresh oranges rotten
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc

                    if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] != 1:
                        continue
                    
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    q.append((new_r, new_c))
            
            minutes += 1
        
        return minutes if fresh == 0 else -1