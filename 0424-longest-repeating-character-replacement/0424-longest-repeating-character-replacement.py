class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use a sliding window that starts with the first char
        # keep expanding the sliding window. Each time, ensure that
        # (the number of characters) - (count of most freq char in the window) <= k
        # that difference tells you how many characters need to be replaced in that curr window
        # if we exceed k, shift l to where r is, and r += 1. shift window over completely

        res = 1
        l = 0
        window_freq = {s[0] : 1}
        most_freq = (s[0], 1)

        for r in range(1, len(s)):
            window_freq[s[r]] = window_freq.get(s[r], 0) + 1
            
            if window_freq[s[r]] > most_freq[1]:
                most_freq = (s[r], window_freq[s[r]])

            if (r - l + 1) - most_freq[1] <= k:
                res = max(res, r - l + 1)
            else:
                window_freq[s[l]] -= 1
                l += 1

        return res