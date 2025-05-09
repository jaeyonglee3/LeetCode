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
                return
            
            grid2[r][c] = 0

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        # first, eliminate all islands in grid2 that are not sub-islands of grid1
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and grid1[r][c] != 1:
                    # if its land on grid2 but not on grid1, the island formed by that
                    # cell is guaranteed to NOT be a valid sub-island
                    print(r, c)
                    dfs(r, c)
        
        # then, count the remaining islands in grid2 (which are guaranteed to be sub-islands)
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1:
                    dfs(r, c)
                    res += 1

        return res