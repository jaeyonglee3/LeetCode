class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS approach:
        # iterate over the entire grid. Any time you encounter an island, increment the total 
        # number of islands. Then, start a DFS search from that island to turn it and all
        # connected 1s into 0s so that we don't count the same island more than once.

        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
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