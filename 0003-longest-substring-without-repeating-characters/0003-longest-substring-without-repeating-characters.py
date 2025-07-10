class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # variable size sliding window problem
        res = 0
        l = 0
        last_seen = {}

        for r in range(len(s)):
            if s[r] in last_seen and last_seen[s[r]] >= l:
                l = last_seen[s[r]] + 1
            
            last_seen[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
