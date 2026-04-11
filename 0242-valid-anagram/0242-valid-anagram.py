class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        for c in s:
            freq_s[c] = freq_s.get(c, 0) + 1
        
        freq_t = {}
        for c in t:
            if c not in freq_s:
                return False
            
            freq_t[c] = freq_t.get(c, 0) + 1

            if freq_t[c] > freq_s[c]:
                return False
        
        return freq_s == freq_t