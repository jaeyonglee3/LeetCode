class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        fresh_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        minutes = 0
        while q and fresh_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc

                    if min(new_r, new_c) < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] != 1:
                        continue
                    
                    # this new cell we are exploring contains a fresh that must be turned rotten
                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c))
                    fresh_count -= 1

            minutes += 1
        
        return minutes if fresh_count == 0 else -1