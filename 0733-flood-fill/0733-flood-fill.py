class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Run a DFS from the starting cell to visit all adjacent cells
        # if the cell we've visited has same pixel value as starting val, change its colour
        ROWS, COLS = len(image), len(image[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        start_val = image[sr][sc]

        def dfs(r, c):
            # Base cases
            if min(r, c) < 0 or r == ROWS or c == COLS or image[r][c] != start_val or image[r][c] == color:
                return
            
            # Otherwise, we're at a cell for which we must change the colour
            image[r][c] = color
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)
        
        dfs(sr, sc)
        return image