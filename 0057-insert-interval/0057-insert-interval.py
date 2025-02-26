class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []  # This will store the final merged intervals

        for i in range(len(intervals)):
            # Case 1: If the curr interval starts AFTER newInterval ends, 
            # there is no overlap, and we can just insert newInterval before it.
            # Since intervals are sorted, all remaining intervals will be non-overlapping.
            if intervals[i][0] > newInterval[1]:  
                res.append(newInterval)
                return res + intervals[i:]
            
            # Case 2: If the current interval ends BEFORE the new interval starts,
            # there is no overlap, so we simply add the current interval to the result.
            elif intervals[i][1] < newInterval[0]:  
                res.append(intervals[i])
            
            # Case 3: The intervals overlap, so we merge them.
            # Update newInterval to the smallest start and largest end between both.
            else:  
                newInterval = [
                    min(newInterval[0], intervals[i][0]),  
                    max(newInterval[1], intervals[i][1])
                ]
        
        # If the newInterval wasn't inserted in the loop (it belongs at the end), add it now.
        res.append(newInterval)
        return res
