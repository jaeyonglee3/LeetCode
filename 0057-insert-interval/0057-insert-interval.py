class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # paraphrase
        # we want to insert newInterval into intervals such that its still sorted in asc order
        # AND there are still no overlapping intervals

        # two intervals overlap if the 2nd one starts before the 1st one ends

        # dry runs (examples)
        # Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        # res = [ (1, 5), (6, 9) ]
        # Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [3,10]
        # res = [ (1,2), (3,10), (12,16) ]

        # approach
        # populate a new result list of intervals by visiting each interval in intervals one at a time
        # 3 cases -> 2 non-overlap cases, 1 overlap case:
            # if it has no overlap at all with newInterval, just add the interval 
            # if it has an overlap, modify newInterval such that it handles the overlap, and continue the process
            # if the new intervals ends before the curr interval starts, there is again no overlap, but now we can just
            # add the new interval to the result, and add the rest of the intervals after it!

        # implement
        res = []

        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
                # overlap detected
                # merge newInterval with interval
                newInterval = (min(newInterval[0], interval[0]), max(newInterval[1], interval[1]))
            elif newInterval[0] > interval[1]:
                res.append(interval)
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                newInterval = None
                res += intervals[i :]
                break
        
        if newInterval:
            res.append(newInterval)
        
        return res