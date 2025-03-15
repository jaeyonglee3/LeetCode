class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # By sorting based on the start time, we guarantee that 
        # no interval with an earlier start appears after an interval with a later start.
        # this will help us merge sequentially in a single pass
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res