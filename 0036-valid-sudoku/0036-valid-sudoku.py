class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        valid_numbers = set("123456789")

        for row_num, row in enumerate(board):
            for col_num, val in enumerate(row):
                if val in valid_numbers:
                    row_copy = rows[row_num].copy()
                    col_copy = cols[col_num].copy()
                    squares_copy = squares[(row_num // 3, col_num // 3)].copy()

                    rows[row_num].add(val)
                    cols[col_num].add(val)
                    squares[(row_num // 3, col_num // 3)].add(val)

                    if (rows[row_num] == row_copy or cols[col_num] == col_copy or squares[(row_num // 3, col_num // 3)] == squares_copy):
                        return False
        
        return True
