class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by start values.
        # This ensures that overlapping intervals are adjacent,
        # making it easier to merge them in the next step.
        intervals.sort()  

        # Step 2: Initialize the result list with the first interval.
        res = [intervals[0]]

        # Step 3: Iterate through the sorted intervals starting from the second one.
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                # The current interval overlaps with the last interval added to res.
                # Merge them by updating rse[-1].
                res[-1][0] = min(intervals[i][0], res[-1][0])
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                # They do not overlap, so add the current interval to the result list.
                res.append(intervals[i])
        
        return res
