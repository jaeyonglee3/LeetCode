class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # want to find the longest window within s in which there are no repeating characters
        # the window's start and end will be marked with l and r pointers
        if len(s) == 0: return 0
        
        res = 1
        l, r = 0, 1
        curr_chars = set([s[l]])

        for r in range(1, len(s)):
            while s[r] in curr_chars:
                curr_chars.remove(s[l])
                l += 1

            res = max(res, r - l + 1)
            curr_chars.add(s[r])
        
        return res