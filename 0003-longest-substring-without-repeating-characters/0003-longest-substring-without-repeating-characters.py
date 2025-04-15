class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l, r = 0, 1
        
        # seen will map the letter to the last index we saw it at
        seen = {s[l] : l}
        res = 1

        while r < len(s):
            if seen.get(s[r], -1) >= l:
                l = seen[s[r]] + 1
            
            seen[s[r]] = r
            res = max(res, r - l + 1)

            r += 1
        
        return res