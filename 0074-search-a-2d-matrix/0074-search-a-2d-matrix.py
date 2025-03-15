class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1) iterate over the rows and find the row that target could fit in
        # 2) do an iterative binary search on that row and return T or F

        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                l, r = 0, len(row) - 1

                while r >= l:
                    mid = (r + l) // 2
                    curr_val = row[mid]

                    if curr_val == target:
                        return True
                    elif curr_val > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                
                return False
        
        return False