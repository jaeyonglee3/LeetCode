class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count_s = {}

        for c in s:
            count_s[c] = 1 + count_s.get(c, 0)
        
        for c in set(t):
            if t.count(c) != count_s.get(c, 0):
                return False

        return True
