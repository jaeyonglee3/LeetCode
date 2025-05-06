class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Use a BFS approach - initialize a queue with the starting cell coordinates
        # at each step of the BFS, popleft from the queue and explore all 4 of that cell's neighbors.
        # If that cell's neighbors have the SAME color as the starting pixel, update that cell's pixel
        # value too and add it to the queue to be processed
        if image[sr][sc] == color: return image

        ROWS, COLS = len(image), len(image[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        og_pixel = image[sr][sc]
        q = collections.deque()
        q.append((sr, sc))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                image[r][c] = color

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or image[nr][nc] != og_pixel:
                        continue
                        
                    q.append((nr, nc))
        
        return image
