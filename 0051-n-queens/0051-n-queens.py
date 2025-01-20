class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # These sets will help us keep track of where we've placed queens
        # -ve diagonals use r - c, +ve diagonals use r + c
        cols, pos_diagonals, neg_diagonals = set(), set(), set()

        res = []
        board = [["."] * n for _ in range(n)] # initialize an empty n x n board filled with dots

        # We'll go row by row starting from 0
        def backtrack(r):
            if r == n:
                # Then we've found a valid solution
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r + c ) in pos_diagonals or (r - c) in neg_diagonals:
                    # Cannot use this r, c position. So, continue
                    continue
                
                # Update all the sets before placing the queen
                cols.add(c)
                pos_diagonals.add(r + c)
                neg_diagonals.add(r - c)
                board[r][c] = "Q"

                # Make the recursive backtrack call
                backtrack(r + 1)

                # Undo all the changes we made to the set to clean up
                # because we're backtracking to try other combos/solutions
                cols.remove(c)
                pos_diagonals.remove(r + c)
                neg_diagonals.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res