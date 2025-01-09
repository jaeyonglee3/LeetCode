class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        cols = [col for col in zip(*board)]

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= len(board) or c >= len(cols) 
                or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))
            res = (backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) 
                    or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1))
            
            path.remove((r, c))
            return res

        # First, starting from the beginning of the grid,
        # iterate to the first letter of the word.
        # Once found, start backtracking algorithm from there
        for r in range(len(board)):
            for c in range(len(cols)):
                if backtrack(r, c, 0):
                    return True
        
        # if loops finish and no solution found
        return False
