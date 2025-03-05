class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        # approach: iterate over every cell.
        # if cell contains a 1, call dfs(r, c) on it and the dfs
        # will return an int representing the area of the island
        # formed by all 4 directionally adjacent cells with value 1
        # connected to the cell from which we started at.

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            
            # set the current position to 0 so its not counted again in the future
            grid[r][c] = 0
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr_area = dfs(r, c)
                    res = max(res, curr_area)
        
        return res