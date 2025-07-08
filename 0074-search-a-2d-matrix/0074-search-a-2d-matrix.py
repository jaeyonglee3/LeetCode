class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find the inner list that can contain target
        # do this with binary search
        # if none is found, return false early
        l, r = 0, len(matrix) - 1
        row = None

        while r >= l:
            mid = (r + l) // 2
            curr_row = matrix[mid]

            if target >= curr_row[0] and target <= curr_row[-1]:
                row = curr_row
                break
            elif target > curr_row[-1]:
                l = mid + 1
            elif target < curr_row[0]:
                r = mid - 1
        
        if row == None:
            return False
        
        l, r = 0, len(matrix[0]) - 1

        while r >= l:
            mid = (r + l) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            else:
                # row[mid] < target
                l = mid + 1
        
        return False
