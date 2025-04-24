class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # approach - we'll define a dfs helper that takes in a r, c position
        # in the grid and performs a dfs starting from that cell. it will
        # return the area of the island that includes the cell at r, c.
        # it will also mark visited island cells as 0s so they're not visited again.
        # we'll iterate over each cell in the grid and call dfs() on each island cell.
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def dfs(r, c) -> int:
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in DIRS:
                area += dfs(r + dr, c + dc)

            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)
        
        return res