class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        atlantic, pacific = set(), set()

        def dfs(r, c, curr_set, prev_height):
            # Base case: r, c is out of bounds, is already in curr_set, or curr height is smaller than prev
            if r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]) or (r, c) in curr_set or heights[r][c] < prev_height:
                return
            
            curr_set.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, curr_set, heights[r][c])
        
        for r in range(len(heights)):
            # we want to dfs on the far left and right columns of the grid
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, len(heights[0]) - 1, atlantic, heights[r][len(heights[0]) - 1])
        
        for c in range(len(heights[0])):
            # we wants to dfs on the top and bottom rows of the grid
            dfs(0, c, pacific, heights[0][c])
            dfs(len(heights) - 1, c, atlantic, heights[len(heights) - 1][c])
        
        # compute the set intersection
        # return the intersection as a list
        res = atlantic.intersection(pacific)
        return list(res)