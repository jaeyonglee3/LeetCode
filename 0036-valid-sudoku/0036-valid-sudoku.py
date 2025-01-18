class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Maps for rows, columns, and sub-boxes
        boxes_map = collections.defaultdict(set)
        rows_map = collections.defaultdict(set)
        cols_map = collections.defaultdict(set)
        
        valid_nums = set("123456789")
        
        for row_num, row in enumerate(board):
            for col_num, val in enumerate(row):
                if val in valid_nums:
                    # Check if the value already exists in row, column, or box
                    if (
                        val in rows_map[row_num] or 
                        val in cols_map[col_num] or 
                        val in boxes_map[(row_num // 3, col_num // 3)]
                    ):
                        return False
                    
                    # Add value to the corresponding maps
                    rows_map[row_num].add(val)
                    cols_map[col_num].add(val)
                    boxes_map[(row_num // 3, col_num // 3)].add(val)
        
        return True
