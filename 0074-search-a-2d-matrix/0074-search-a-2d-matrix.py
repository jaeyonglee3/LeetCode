class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while r >= l:
            mid = (l + r) // 2
            row, col = mid // COLS, mid % COLS
            curr_val = matrix[row][col]

            if curr_val == target:
                return True
            elif curr_val > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False