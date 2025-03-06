class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []  # This will store the final merged intervals

        # we'll iterate over every interval and run some checks to determine
        # what to / not to do with newInterval.

        # a merge needs to happen between two intervals if one's start value
        # is lesser than the other's end value.

        for i in range(len(intervals)):
            curr = intervals[i]
            # case 1: NO OVERLAP
            # the curr interval starts after the newInterval ends
            # then, we can add new interval to the result, followed by the rest of the intervals
            # after the curr one (no overlaps would happen b/c intervals is sorted by start)
            if curr[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i : ]

            # case 2: NO OVERLAP
            # the curr interval ends before the newInterval starts
            # there could possibly be intervals that follow the curr one that would overlap
            # with newInterval. Here, only add the curr interval to res and do nothing else.
            elif curr[1] < newInterval[0]:
                res.append(curr)

            # case 3: OVERLAP
            # then, we'll modify the newInterval to reflect a merge between itself and curr
            # interval. Its important that we modify newInterval, not curr, b/c our cases
            # rely on comparisons with the newInterval.
            else:
                newInterval = [min(curr[0], newInterval[0]), max(curr[1], newInterval[1])]
        
        res.append(newInterval)
        return res