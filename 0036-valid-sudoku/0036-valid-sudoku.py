class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue

                sq_r, sq_c = r // 3, c // 3

                if val in rows[r] or val in cols[c] or val in squares[(sq_r, sq_c)]:
                    print((r, c))
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[(sq_r, sq_c)].add(val)
        
        return True