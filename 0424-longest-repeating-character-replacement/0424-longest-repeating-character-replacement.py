class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # in other words
        # let most_freq denote the most frequent character in a given substring s_string
        # so, we want to know the length of the longest substring in s (s_string)
        # such that len(s_string) minus all instances of most_freq is at most k

        res = 0
        freq_map = {}  # maps frequency of each letter in current substring s[l : r + 1]
        most_freq = 1  # the count of the most frequent character in the substring

        l = 0
        for r in range(len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1

            most_freq = max(most_freq, freq_map[s[r]])

            s_string_len = r - l + 1

            while (r - l + 1) - most_freq > k:
                # s_string is no longer valid
                freq_map[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res