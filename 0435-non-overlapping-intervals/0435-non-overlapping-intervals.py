class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair : pair[1])
        res = 0
        prev_end = -math.inf

        for start, end in intervals:
            if start < prev_end:
                res += 1
            else:
                prev_end = end
        
        return res