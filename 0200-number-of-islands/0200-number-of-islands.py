class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # Use some dfs technique to change all connected 1s as 0s
                    # this effectively marks all the connected 1 cells as "visited"
                    # this ensures we count each island only once
                    res += 1
                    dfs(r, c)
        
        return res