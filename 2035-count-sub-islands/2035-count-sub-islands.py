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
            
            # print(r, c)
            grid2[r][c] = 0
            valid = grid1[r][c] == 1

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                new_valid = dfs(nr, nc)
                valid = valid and new_valid
            
            return valid
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1:
                    # print((r, c))
                    valid = dfs(r, c)
                    if valid:
                        print(r, c)
                    res += 1 if valid else 0

        return res