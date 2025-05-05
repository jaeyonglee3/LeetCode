class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # For each land cell, assume it contributes 4 to the perimeter
        # but subtract 1 for every adjacent land cell it shares an edge with.
        # Define a dfs() helper function that returns the total perimeter.
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c) -> int:
            if (r, c) in visited:
                return 0

            curr_perm = 4
            visited.add((r, c))
            neighboring_land = []

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0:
                    continue

                curr_perm -= 1
                neighboring_land.append((nr, nc))
            
            for nr, nc in neighboring_land:
                curr_perm += dfs(nr, nc)
            
            return curr_perm
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)