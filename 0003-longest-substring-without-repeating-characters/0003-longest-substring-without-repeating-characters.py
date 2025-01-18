class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        l = 0
        res = 0

        for r in range(len(s)):
            char = s[r]

            # If the current character (char) is already in visited and 
            # its last seen index is within the current window,
            # a duplicate has been found
            if char in visited and visited[char] >= l:
                # shrink window by moving left to just one after the last place
                # we saw it. this leaves out only the duplicate
                l = visited[char] + 1
            else:
                # no duplicates, so the current window contains a valid substring
                res = max(res, r - l + 1)
            
            visited[char] = r
        
        return res