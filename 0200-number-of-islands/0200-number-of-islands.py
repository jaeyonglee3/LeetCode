class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        for row_num, row in enumerate(grid):
            for col_num, val in enumerate(row):
                if val == "1":
                    res += 1
                    dfs(row_num, col_num)
        
        return res