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
                l = visited[char] + 1 # shrink window to leave out duplicate
            else:
                # no duplicate found, curr window contains a valid substring
                res = max(res, r + 1 - l)
            
            visited[char] = r
        
        return res
