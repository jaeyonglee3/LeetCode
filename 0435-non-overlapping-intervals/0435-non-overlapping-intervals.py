class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            # edge case
            return 0

        # sort by start times to put all overlapping intervals next to each other
        intervals.sort(key=lambda interval : interval[0])
        last_interval = intervals[0]

        res = 0

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if interval[0] < last_interval[1]:
                # we have an overlap, so increment result
                res += 1
                last_interval = last_interval if last_interval[1] < interval[1] else interval
            else:
                last_interval = interval
        
        return res

        # [[1,100],[11,22],[1,11],[2,12]]
        # [[1,11],[1,100],[11,22],[2,12]]