class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS approach - call a dfs() helper on each cell that contains the starting letter
        # run a dfs, keeping track of which char in the word is being looked for
        # and also the current "path" of cell coordinates.
        # if the last letter of the word is reached, we have a valid path of letters
        # that together form the word, and therefore can return true.
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, i, path) -> bool:
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in path or board[r][c] != word[i]:
                return False
            if i == len(word) - 1 and board[r][c] == word[i]:
                return True
            
            path.add((r, c))
            for dr, dc in DIRS:
                if dfs(r + dr, c + dc, i + 1, path):
                    return True
            
            path.pop()
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True
        
        return False