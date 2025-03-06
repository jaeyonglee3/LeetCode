class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        # visit every cell. If we have a 1, run a DFS on it that would visit all
        # adjacent 1s, marking them as zeros so as they are not visited again.
        # once this is complete, increment res += 1 since we've successfully visited
        # just one island. All separate islands remain intact.

        def dfs(r, c):
            # the purpose of this dfs is to mark grid[r][c] and all adjacent 1s as 0s
            # so that they're not visited again and mistakenly counted as separate, unqiue islands.
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)
            
            return
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        
        return res
