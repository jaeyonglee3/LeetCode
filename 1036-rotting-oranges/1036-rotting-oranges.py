class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque()
        fresh = 0
        minutes = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    # Count number of fresh oranges
                    fresh += 1
                if grid[r][c] == 2:
                    # Add all rotten oranges to queue
                    q.append((r, c))
        
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            
            minutes += 1

        if fresh > 0:
            return -1
        
        return minutes