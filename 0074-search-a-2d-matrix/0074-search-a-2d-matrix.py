class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                # Perform binary search on that row
                # Return true if found, false otherwise
                return self.binSearch(row, target)
        
        # No row in the matrix can possibly contain target
        return False
    
    def binSearch(self, row, target) -> bool:
        l, r = 0, len(row) - 1

        while r >= l:
            mid = (r + l) // 2

            if target == row[mid]:
                return True
            elif target > row[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
            
            
        