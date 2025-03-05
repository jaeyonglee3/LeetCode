class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # step 1: sort the intervals arr by start values so that any
        # overlapping intervals are next to each other.
        intervals.sort()
        res = 0
        curr_end = intervals[0][1]

        for i in range(1, len(intervals)):
            # an overlap occurs between two intervals when one of their start times
            # is lesser than the other's end time.
            if intervals[i][0] < curr_end:
                res += 1
                # take the min since its less likely to overlap with other intervals.
                curr_end = min(curr_end, intervals[i][1])
            else:
                curr_end = intervals[i][1]
        
        return res
