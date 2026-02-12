class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0

        for l in range(len(s)):
            unique_chars = {}
            
            for r in range(l, len(s)):
                curr_char = s[r]
                unique_chars[curr_char] = unique_chars.get(curr_char, 0) + 1

                vals = set(unique_chars.values())
                if len(vals) == 1:
                    res = max(res, r - l + 1)
        
        return res
