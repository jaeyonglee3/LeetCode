class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by ascending order by start values because this would put
        # any overlapping intervals next to each other
        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        
        return res
