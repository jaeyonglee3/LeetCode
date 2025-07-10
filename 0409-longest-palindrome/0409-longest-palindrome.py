class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        count = {}
        extra = 0

        for c in s:
            count[c] = count.get(c, 0) + 1

        if len(count) == 1:
            return len(s)

        for val in count.values():
            if val % 2 == 0:
                res += val
            else:
                res += val - 1
                extra = 1
        
        return res + extra