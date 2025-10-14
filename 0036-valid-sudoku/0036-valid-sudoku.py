class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # looking for repetition, so use sets for O(1) additions and membership checks
        # each dict will have key for row/col num, then each val will be the set of nums
        ROWS, COLS = len(board), len(board[0])
        rows, cols, subsquares = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    # we are only concerned with validating filled cells
                    continue
                
                curr_val = int(board[r][c])
                subsquare_num = (r // 3 , c // 3)

                if curr_val in rows[r]: return False
                if curr_val in cols[c]: return False
                if curr_val in subsquares[subsquare_num]: return False

                rows[r].add(curr_val)
                cols[c].add(curr_val)
                subsquares[subsquare_num].add(curr_val)
            
        return True