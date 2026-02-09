class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]

                if val == ".":
                    continue
                
                square_index = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in squares[square_index]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[square_index].add(val)
        
        return True
