class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])

        # any O region that is not connected to an edge cell of the board
        # will be turned into an X.
        # dfs on any O edge cell to visit its entire region of connected Os
        # and mark them with a temporary T. once that is done, make the changes to the board.
        # all Ts will becomes Os again, and all Os will become Xs

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'