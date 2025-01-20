class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Idea is to start at the very edges and DFS into the board
        # Two sets, atlantic and pacific, will keep track of which cells can access them
        # and at the end, we'll return an intersection of the two sets
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        def dfs(r, c, curr_set, prev_height):
            # curr_set is the set we are currently working with
            # prev_height will help us determine if we should continue recursing
            # (we're going backwards, from ocean to inwards, so curr height must be >= prev_height)
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prev_height or (r, c) in curr_set:
                return
            
            # add the current (r, c) coords to our current working set
            curr_set.add((r, c))

            # then make recursive dfs calls in all 4 directions to continue adding to the set
            for dr, dc in directions:
                curr_height = heights[r][c]
                dfs(r + dr, c + dc, curr_set, curr_height)
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # return the intersection between atlantic and pacific sets
        # b/c those are the cells that can flow to both oceans
        result = atlantic.intersection(pacific)
        return list(result)