class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # paraphrase
        # we want to find the substring with the most # of occurrences
            # it can have at most maxLetters
            # its length must be between [minSize, maxSize]
        # maxSize is at most 26

        # Input: s = "aababcaab"
        
        diff = maxSize - minSize
        l, r = 0, minSize - 1
        freq = {}

        while r < len(s):
            for end_i in range(r, r + diff + 1):
                if end_i >= len(s):
                    break
                
                substring = s[l : end_i + 1]
                if len(set(substring)) <= maxLetters:
                    freq[substring] = freq.get(substring, 0) + 1
                
            l += 1
            r += 1
        
        return max(freq.values()) if freq else 0