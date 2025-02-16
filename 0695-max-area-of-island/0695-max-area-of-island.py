class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def dfs(r, c) -> int:
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for row_num, row in enumerate(grid):
            for col_num, val in enumerate(row):
                if val == 1:
                    area = dfs(row_num, col_num)
                    res = max(area, res)
        
        return res