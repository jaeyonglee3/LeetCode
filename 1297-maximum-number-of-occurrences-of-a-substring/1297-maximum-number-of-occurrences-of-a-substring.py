class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # sstrings = []
        # count = {}

        # while minSize <= maxSize:
        #     for i in range(len(s)):
        #         if (i + minSize) <= len(s) and len(set(s[i : i + minSize])) <= maxLetters:
        #             sstrings.append(s[i: i + minSize])
            
        #     minSize += 1
        
        # for sstring in sstrings:
        #     count[sstring] = count[sstring] + 1 if sstring in count else 1

        # return max(count.values()) if count else 0

        # count frequency of characters
        count = collections.Counter()
        
        # Check only for minSize
        for i in range(len(s) - minSize + 1):
            t = s[i : i+minSize]
            if len(set(t)) <= maxLetters:
                count[t] += 1
        
        return max(count.values()) if count else 0