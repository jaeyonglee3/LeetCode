class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS approach: visit every cell. If the cell is an island,
        # DFS starting from that cell and mark each connected "1" as "0"
        # so that we don't count that same island twice
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        
        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return
            
            # mark this current cell as water
            grid[r][c] = "0"
            for dr, dc in DIRS:
                dfs(r + dr, c + dc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        return res