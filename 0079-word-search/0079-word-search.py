class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, r, c):
            # Base case
            if i >= len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r, c) in path:
                return False
            
            # DFS body
            path.add((r, c))
            for dr, dc in directions:
                if dfs(i + 1, r + dr, c + dc):
                    return True
            
            path.remove((r, c))
            return False
        
        for row_num, row in enumerate(board):
            for col_num in range(COLS):
                if dfs(0, row_num, col_num):
                    return True
        
        return False