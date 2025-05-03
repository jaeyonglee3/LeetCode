class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # the result contains all coordinates from which water can flow into both oceans
        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific, atlantic = set(), set()

        def dfs(r, c, curr_set, prev_h):
            if min(r, c) < 0 or r == ROWS or c == COLS or prev_h > heights[r][c] or (r, c) in curr_set:
                return
            
            curr_set.add((r, c))
            for dr, dc in DIRS:
                new_r, new_c = r + dr, c + dc
                dfs(new_r, new_c, curr_set, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, -1)
            dfs(r, COLS - 1, atlantic, -1)
        
        for c in range(COLS):
            dfs(0, c, pacific, -1)
            dfs(ROWS - 1, c, atlantic, -1)
        
        return list(atlantic.intersection(pacific))

        # time: O(m * n)
        # space: O(m * n)
        # Where m is the number of rows and n is the number of columns.