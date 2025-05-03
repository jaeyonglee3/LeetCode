class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Multi-source BFS Approach
        # We'll have a coordinate queue that starts with all edge cells containing Os
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque()

        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][COLS - 1] == "O":
                q.append((r, COLS - 1))
        
        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0, c))
            if board[ROWS - 1][c] == "O":
                q.append((ROWS - 1, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                board[r][c] = "T"

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or board[nr][nc] != "O":
                        continue
                    
                    q.append((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
