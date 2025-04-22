class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # We can iterate over the board. Each time we hit an X,
        # we increment result by 1 and DFS from that position to mark
        # the entire ship as visited by marking them with a "." so we can
        # avoid counting a single ship more than once.

        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or board[r][c] == ".":
                return
            
            board[r][c] = "."
            for dr, dc in DIRS:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X":
                    res += 1
                    dfs(r, c)
        
        return res