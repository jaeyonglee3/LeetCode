class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first, find the row the target could fit into
        for row in matrix:
            if row[0] <= target and target <= row[-1]:
                # the target must be in this row
                # perform a binary search on this row
                l, r = 0, len(row) - 1

                while l <= r:
                    mid = (l + r) // 2

                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                
                return False
        
        return False