class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # can solve with BFS
        if image[sr][sc] == color: return image

        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(image), len(image[0])
        og_color = image[sr][sc]

        def dfs(r, c) -> None:
            if min(r, c) < 0 or r == ROWS or c == COLS or image[r][c] != og_color:
                return
            
            image[r][c] = color
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        dfs(sr, sc)
        return image