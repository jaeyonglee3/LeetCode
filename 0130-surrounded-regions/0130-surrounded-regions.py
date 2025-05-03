class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS approach
        # iterate over / visit all the edge cells
        # if that cell is an "O" mark it with a special temp character "T"
        # then, run a DFS with that cell as the starting point to find every
        # "O" that is connected to it. Mark them all with Ts
        # At the end, iterate over the entire board. Make all Os into Xs
        # and all Ts back into Os

        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            # Base case
            if min(r, c) < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            for dr, dc in DIRS:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        # Now, modify the board appropriately
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
