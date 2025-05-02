class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # the result contains all coordinates from which water can flow into both oceans
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, prev_h, curr_set):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in curr_set or heights[r][c] < prev_h:
                return
            
            # otherwise, that current r, c can reach that ocean
            curr_set.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], curr_set)

        for r in range(ROWS):
            dfs(r, 0, -1, pacific)
            dfs(r, COLS - 1, -1, atlantic)
        
        for c in range(COLS):
            dfs(0, c, -1, pacific)
            dfs(ROWS - 1, c, -2, atlantic)
        
        result = pacific.intersection(atlantic)
        return list(result)
        
        

