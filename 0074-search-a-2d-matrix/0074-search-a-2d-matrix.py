class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        is_row_found = False

        while bot >= top:
            row_idx = (top + bot) // 2
            row = matrix[row_idx]
            
            if target > row[-1]:
                top = row_idx + 1
            elif target < row[0]:
                bot = row_idx - 1
            else:
                is_row_found = True
                break
        
        if not is_row_found:
            return False
        
        row = matrix[(top + bot) // 2]
        l, r = 0, COLS - 1

        while r >= l:
            mid = (l + r) // 2
            curr_val = row[mid]

            if curr_val == target:
                return True
            elif curr_val > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
                