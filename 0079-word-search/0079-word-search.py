class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(i, r, c, path):
            if i > len(word) - 1:
                return True
            if min(r, c) < 0 or r == ROWS or c == COLS or board[r][c] != word[i] or (r, c) in path:
                return False
            
            path.add((r, c))
            # Now, explore 4-directionally and make recursive calls
            for dr, dc in DIRECTIONS:
                if dfs(i + 1, r + dr, c + dc, path):
                    return True
            
            # no matter how deep into the path we are, this is the same path variable
            # from the letter we started with. Remove is necessary to reset the path
            # back to normal after trying a bad path.
            path.remove((r, c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c, set()):
                    return True
        
        return False