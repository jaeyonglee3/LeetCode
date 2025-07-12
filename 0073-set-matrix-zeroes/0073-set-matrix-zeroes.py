class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # iterate over matrix and create two lists, rows and cols
            # rows contains the row values of all rows that contain at least 1 zero
            # cols contains the col values of all cols that contain at least 1 zero
        # with those arrays, modify matrix in-place

        # space optimization - for O(1) extra space
        # use the first row and first col as indicators
        ROWS, COLS = len(matrix), len(matrix[0])
        zero_first_row, zero_first_col = False, False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        zero_first_row = True
                    if c == 0:
                        zero_first_col = True
                    
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # modify the matrix in-place
        for r in range(1, ROWS):
            if matrix[r][0] == 0:
                matrix[r] = [0] * COLS
        
        for c in range(1, COLS):
            if matrix[0][c] == 0:
                for r in range(ROWS):
                    matrix[r][c] = 0
        
        # if the first row or first col themselves need to be zeroes,
        # take care of it here
        if zero_first_row:
            matrix[0] = [0] * COLS
        
        if zero_first_col:
            for r in range(ROWS):
                matrix[r][0] = 0