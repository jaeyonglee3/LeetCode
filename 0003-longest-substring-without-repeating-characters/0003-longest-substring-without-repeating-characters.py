class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0, 1 
        seen = {s[0] : 0}
        res = 1

        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            
            res = max(res, r - l + 1)
            seen[s[r]] = r
            r += 1
        
        return res