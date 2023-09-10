class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = collections.Counter()
        
        # Check only for minSize
        for i in range(len(s) - minSize + 1):
            t = s[i : i+minSize]
            if len(set(t)) <= maxLetters:
                count[t] += 1
        
        return max(count.values(), default = 0)