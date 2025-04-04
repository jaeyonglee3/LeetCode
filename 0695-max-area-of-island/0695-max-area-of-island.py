class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c) -> int:
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(dfs(r, c), res)
        
        return res