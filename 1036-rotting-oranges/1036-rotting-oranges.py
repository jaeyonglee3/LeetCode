class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Can solve using BFS
        # Initial setup - count # of fresh oranges and add all
        # rotten oranges to a queue
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque() # contains only rotten oranges
        fresh = 0
        minutes = 0

        for row_num, row in enumerate(grid):
            for col_num, val in enumerate(row):
                if val == 1:
                    fresh += 1
                if val == 2:
                    q.append((row_num, col_num))

        # Ready now to begin BFS traversal
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:  
                    row, col = r + dr, c + dc

                    if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1 :
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
            
            minutes += 1
        
        return minutes if fresh == 0 else -1