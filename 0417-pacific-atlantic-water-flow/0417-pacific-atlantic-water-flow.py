class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, curr_set, prev_height):
            if (r, c) in curr_set or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prev_height:
                return
            
            curr_set.add((r, c))
            for dr, dc in directions:
                curr_height = heights[r][c]
                dfs(r + dr, c + dc, curr_set, curr_height)

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        result = pacific.intersection(atlantic)
        return list(result)