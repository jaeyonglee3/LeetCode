class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        cols = [col for col in zip(*board)]

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= len(board) or c >= len(cols)
                or (r, c) in path or word[i] != board[r][c]):
                return False
            
            # Base cases have passed so add to path
            path.add((r, c))

            # Make recursive calls to all 4 possible directions
            new = i + 1
            res = (backtrack(r + 1, c, new) or backtrack(r - 1, c, new) or 
            backtrack(r, c + 1, new) or backtrack(r, c - 1, new))

            # Remove to ensure backward is considered too (r to l connection)
            path.remove((r, c))
            # If res is true that means we've found a valid path!
            # i.e. if even one of the backtracks are true
            return res
        
        for row in range(len(board)):
            for col in range(len(cols)):
                if backtrack(row, col, 0):
                    return True
        
        return False
