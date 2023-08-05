class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window technique, O(n) time
        visited = {}  # char:last known index
        l_pointer = 0
        max_len = 0

        for r_pointer in range(len(s)):
            char = s[r_pointer]

            # Check if we've seen the char before 
            # and if last known index is >= l_pointer
            if char in visited and visited[char] >= l_pointer:
                l_pointer = visited[char] + 1
            else:
                max_len = max(max_len, r_pointer + 1 - l_pointer)
            visited[char] = r_pointer
        
        return max_len
