class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0  # Left pointer
        char_set = set()  # To track unique characters in the current window
        res = 0  # Store the maximum length of substring

        for r in range(len(s)):  # Right pointer iterates over the string
            # If the character is already in the set, shrink the window from the left
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            # Add the current character to the set
            char_set.add(s[r])
            # Update the result with the current window size
            res = max(res, r - l + 1)

        return res
