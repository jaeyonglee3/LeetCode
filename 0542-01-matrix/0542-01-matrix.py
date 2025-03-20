class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        new_mat = [[-1] * COLS for _ in range(ROWS)]
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    new_mat[r][c] = 0
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()

            for dr, dc in DIRS:
                new_r, new_c = r + dr, c + dc

                if min(new_r, new_c) < 0 or new_r == ROWS or new_c == COLS or new_mat[new_r][new_c] != -1:
                    continue
                
                new_mat[new_r][new_c] = new_mat[r][c] + 1
                q.append((new_r, new_c))
        
        return new_mat

        # time: O(m * n) b/c each cell is processed once

        # space: O(m * n)
        # In the worst case, queue holds all m * n cells