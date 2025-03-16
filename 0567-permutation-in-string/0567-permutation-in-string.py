class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = collections.defaultdict(int)
        for c in s1:
            freq_s1[c] += 1

        l, r = 0, len(s1) - 1
        while r < len(s2):
            freq_s2 = collections.defaultdict(int)
            for c in s2[l : r + 1]:
                freq_s2[c] += 1
            
            if freq_s1 == freq_s2:
                return True
            
            l += 1
            r += 1
        
        return False