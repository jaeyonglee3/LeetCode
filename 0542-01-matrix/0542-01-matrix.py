from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    # all unexplored 1 cells start off as -1
                    mat[r][c] = -1
        
        while q:
            r, c = q.popleft()

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
        
        return mat