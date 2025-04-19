class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-source BFS approach
        # implemented with a queue that always contains all rotten cell coordinates
        # at each "minute" (iteration), we'll check 4-directionally from all cells in queue
        # and handle them accordingly
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        num_fresh = 0

        # step 1 - fill the queue with all rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    num_fresh += 1
        
        # step 2 - process each rotten orange, one at a time
        # look 4 directionally from each one, making any adjacent fresh oranges rotten
        num_minutes = 0
        while q and num_fresh:
            num_minutes += 1
            
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIRS:
                    new_r, new_c = r + dr, c + dc

                    if min(new_r, new_c) < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] != 1:
                        continue
                    
                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c))
                    num_fresh -= 1
        
        return num_minutes if num_fresh == 0 else -1