class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = set()

        for c in s:
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)
        
        if len(chars) == 0:
            return len(s)

        return len(s) - (len(chars) - 1)
