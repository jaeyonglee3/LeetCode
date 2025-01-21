class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def dfs(r, c):
            # BASE CASE
            # r, c numbers are out of bounds OR grid[r][c] == "0"
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
            
            # Mark the current cell as 0 so its not visited again
            grid[r][c] = "0"
            
            # Check every direction (up, down, left, right) from the current r, c position
            for direction in directions:
                dfs(r + direction[0], c + direction[1])

        for row_num, row in enumerate(grid):
            for col_num, val in enumerate(row):
                if val == "1":
                    # DFS on that island to mark all its connected 1s
                    # so that connected 1s aren't mistakenly counted as separate islands!
                    dfs(row_num, col_num)
                    res += 1
        
        return res