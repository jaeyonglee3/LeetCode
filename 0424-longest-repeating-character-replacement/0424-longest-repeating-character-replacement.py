class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # key insight 1: use a sliding window to go over substrings in s
        # and find the longest one that can be made of the same letter with k operations

        # key insight 2: to calculate the number of operations needed in a window,
        # use len(current window) minus number of the most frequent character in that window.

        if not s:
            return 0
        
        res = 1
        char_freq = {s[0] : 1}
        most_freq = (s[0], 1)
        l = 0

        for r in range(1, len(s)):
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1

            if char_freq[s[r]] > most_freq[1]:
                most_freq = (s[r], char_freq[s[r]])
            
            # calculate the number of operations needed in window
            num_ops = (r - l + 1) - most_freq[1]

            if num_ops <= k:
                res = max(res, (r - l + 1))
            else:
                char_freq[s[l]] -= 1
                l += 1
        
        return res