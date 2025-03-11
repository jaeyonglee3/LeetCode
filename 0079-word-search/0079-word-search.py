class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(i, r, c, path):
            if i > len(word) - 1:
                return True
            if r < 0 or c < 0 or r == ROWS or c == COLS or word[i] != board[r][c] or (r, c) in path:
                return False
            
            path.add((r, c))
            for dr, dc in DIRECTIONS:
                if dfs(i + 1, r + dr, c + dc, path):
                    return True
            
            path.remove((r, c))
            return False
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c, set()):
                    return True
        
        return False