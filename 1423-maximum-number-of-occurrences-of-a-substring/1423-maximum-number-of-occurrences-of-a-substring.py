class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # paraphrase
        # we want to find the substring with the most # of occurrences
            # it can have at most maxLetters
            # its length must be between [minSize, maxSize]
        # maxSize is at most 26
        l = 0
        freq = {}
        res = 0

        for r in range(minSize - 1, len(s)):
            substring = s[l : r + 1]
            if len(set(substring)) <= maxLetters:
                freq[substring] = freq.get(substring, 0) + 1
                res = max(res, freq[substring])
                
            l += 1
        
        return res