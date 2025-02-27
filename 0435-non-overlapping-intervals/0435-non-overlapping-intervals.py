class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # overlap detected
                # it makes sense to "delete" the one with the bigger range because
                # that one is more likely to overlap with other intervals.
                # we set prev_end to min of both ending values.
                # the interval that is "wider," i.e. had bigger end value, is effectively ignored
                prev_end = min(end, prev_end)
                res += 1
            else:
                prev_end = end
        
        return res