class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        visited = {}

        for r in range(len(s)):
            char = s[r]

            if char in visited and visited[char] >= l:
                l = visited[char] + 1
            else:
                res = max(res, r - l + 1)
        
            visited[char] = r
        
        return res

