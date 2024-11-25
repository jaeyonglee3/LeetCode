class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        l = 0
        res = 0

        for r in range(len(s)):
            char = s[r]

            if char in visited and visited[char] >= l:
                l = visited[char] + 1
            else:
                res = max(res, r + 1 - l)
            
            visited[char] = r
        
        return res

