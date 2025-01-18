class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # For each 3x3 box, we'll use the top left corner value as a unique identifier to store
        # the values belonging to the subbox
        boxes_map = collections.defaultdict(set)
        rows_map = collections.defaultdict(set)
        cols_map = collections.defaultdict(set)
        valid_nums = set("123456789")

        for row_num, row in enumerate(board):
            for col_num, val in enumerate(row):
                if val in valid_nums:
                    # before adding to the maps, create copies of them to see if it grows or not
                    row_copy = rows_map[row_num].copy()
                    col_copy = cols_map[col_num].copy()
                    boxes_map_copy = boxes_map[(row_num // 3, col_num // 3)].copy()
                    
                    # add it to the maps and continue
                    rows_map[row_num].add(val)
                    cols_map[col_num].add(val)
                    boxes_map[(row_num // 3, col_num // 3)].add(val)

                    if (rows_map[row_num] == row_copy or cols_map[col_num] == col_copy or boxes_map[(row_num // 3, col_num // 3)] == boxes_map_copy):
                        return False
        
        return True