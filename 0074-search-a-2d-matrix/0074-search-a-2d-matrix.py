class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find the inner list that can contain target
        # do this with binary search
        # if none is found, return false early
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while r >= l:
            mid = (r + l) // 2
            row, col = mid // COLS, mid % COLS
            curr_val = matrix[row][col]

            if curr_val == target:
                return True
            elif curr_val > target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False