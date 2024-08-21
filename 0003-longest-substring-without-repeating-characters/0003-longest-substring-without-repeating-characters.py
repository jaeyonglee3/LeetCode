class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window technique, O(n) time
        visited = {}  # char:last known index
        l_ptr = 0
        greatest_len = 0

        for r_ptr in range(len(s)):
            char = s[r_ptr]

            if char in visited and visited[char] >= l_ptr:
                l_ptr = visited[char] + 1
            else:
                greatest_len = max(greatest_len, r_ptr + 1 - l_ptr)
            visited[char] = r_ptr
        
        return greatest_len
    