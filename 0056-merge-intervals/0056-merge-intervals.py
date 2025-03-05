class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # step 1: sort all intervals so that any overlapping ones are adjacent
        intervals.sort()
        res = [intervals[0]]

        # an overlap occurs between two intervals if one of their start time
        # is lesser than or equal to the other's end time

        # step 2: iterate over the intervals and merge any overlaps
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                # only update the end time to be the bigger between the two
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        
        return res
