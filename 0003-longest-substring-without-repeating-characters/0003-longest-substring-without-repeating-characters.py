class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        res = 0

        for r, c in enumerate(s):
            # If the current character (char) is already in visited and 
            # its last seen index is within the current window,
            # a duplicate has been found
            if c in seen and seen[c] >= l:
                # shrink window by moving left to just one after the last place
                # we saw it. this leaves out only the duplicate
                l = seen[c] + 1
            else:
                # no duplicates, so the current window contains a valid substring
                res = max(res, r - l + 1)
            
            seen[c] = r
        
        return res