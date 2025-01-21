class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            # Base Case
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == "X" or board[r][c] == "T":
                return
            
            # Set the cell at (r, c) to some temporary character
            board[r][c] = "T"

            # Make recursive calls in all 4 directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # Invoke a dfs call on all the boarder cells
        # to mark all unsurrounded regions (reverse thinking!)
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        # Now, iterate over entire board. Set all O's to X's and all T's to O's
        # B/c at this point, T's are all the unsurrounded cells as marked by our DFS
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"