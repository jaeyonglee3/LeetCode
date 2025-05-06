class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # Similar to number of islands
        # Lets iterate over the grid and when we encounter a land cell, we'll call a DFS helper.
        # Initialize a result variable at 0.
        # dfs(r, c) will mark the current cell as 0 to mark as visited, and then will look 4
        # directionally from it.
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c) -> (int, bool):
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return (0, False)
            if grid[r][c] == 0:
                return (0, True)
            
            grid[r][c] = 0
            curr_size, is_valid = 1, True

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                size, new_is_valid = dfs(nr, nc)
                
                curr_size += size
                is_valid = is_valid and new_is_valid
                
            return (curr_size, is_valid)
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    size, is_valid = dfs(r, c)
                    res += size if is_valid else 0
        
        return res