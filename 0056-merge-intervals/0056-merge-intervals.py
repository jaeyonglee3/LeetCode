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
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res
