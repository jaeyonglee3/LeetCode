class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def dfs(r, c) -> None:
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr, dc in DIRS:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        return res