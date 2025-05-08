class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # similar to number of islands
        # except we only count the island in grid 2 if it is completely comprised
        # of cell coordinates which are also land cells in grid 1

        ROWS, COLS = len(grid1), len(grid1[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid2[r][c] == 0:
                return True
            
            grid2[r][c] = 0
            valid = grid1[r][c] == 1

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # THIS DOESN'T WORK: valid = valid and dfs(nr, nc)
                # this evaluates dfs(nr, nc) only if valid is already True due to Python's short-circuiting 
                # in and operations. So if valid is False at any point, the dfs() won't even be called for 
                # future neighbors — which means you're potentially skipping parts of the island 
                # and not marking them as visited.
                new_valid = dfs(nr, nc)
                valid = valid and new_valid
            
            return valid
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1:
                    valid = dfs(r, c)
                    res += 1 if valid else 0

        return res