class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # want to find the longest window within s in which there are no repeating characters
        # the window's start and end will be marked with l and r pointers
        
        # if the right is pointing to a character that is already inside the window,
        # move the left pointer to the index of the repeated character + 1. R ptr still increments by 1 as usual.
        # Take 'azzbcbb' as an example. When right is pointing to the 2nd last b, left needs to move up all the way to index 4
        
        # Edge case - an empty string will always return 0
        if len(s) == 0: 
            return 0
        
        l = 0
        last_seen = {s[l] : 0}  # maps characters to their last seen index
        res = 1

        for r in range(1, len(s)):
            if last_seen.get(s[r], -1) >= l:
                l = last_seen[s[r]] + 1

            last_seen[s[r]] = r
            res = max(res, r - l + 1)
        
        return res