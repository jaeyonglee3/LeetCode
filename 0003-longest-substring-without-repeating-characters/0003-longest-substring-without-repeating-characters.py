class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        res = 0

        for r, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            else:
                res = max(res, r - l + 1)
            
            seen[c] = r
        
        return res