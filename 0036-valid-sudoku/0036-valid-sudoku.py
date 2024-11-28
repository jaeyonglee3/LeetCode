class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        valid_numbers = set("123456789")

        for row_num, row in enumerate(board):
            for col_num, val in enumerate(row):
                if val in valid_numbers:
                    if (val in rows[row_num] or val in cols[col_num] or val in squares[(row_num // 3, col_num // 3)]):
                            return False

                    # If no duplicate, add val to the sets
                    rows[row_num].add(val)
                    cols[col_num].add(val)
                    squares[(row_num // 3, col_num // 3)].add(val)

        return True  # If no duplicates were found, the board is valid