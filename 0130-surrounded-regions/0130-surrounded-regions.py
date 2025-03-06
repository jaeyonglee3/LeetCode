class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # essentially, any 'O' cell group that is not connected to an 'O'
        # cell that is at the edge of the board needs to be turned into an 'X'

        # we'll dfs from every 'O' edge cell and mark all connected 'O's with
        # some temp character. at the end, visit every cell, turn all temp cells
        # backl into 'O's and every other 'O' cell into 'X's b/c they aren't connected
        # to any 'O' that is at the edge of the grid

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)
            
            return
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        
