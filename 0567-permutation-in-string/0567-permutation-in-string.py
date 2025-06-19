class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or len(s2) == 0:
            return False

        s1_freq = {}
        for c in s1:
            s1_freq[c] = s1_freq.get(c, 0) + 1

        l, r = 0, 1
        substring_freq = {s2[0] : 1}
        while r < len(s1):
            substring_freq[s2[r]] = substring_freq.get(s2[r], 0) + 1
            r += 1
        
        r = len(s1) - 1
        while r < len(s2) and substring_freq != s1_freq:
            substring_freq[s2[l]] -= 1
            if substring_freq[s2[l]] == 0:
                del substring_freq[s2[l]]
            
            l += 1
            r += 1

            if r > len(s2) - 1:
                return False

            substring_freq[s2[r]] = substring_freq.get(s2[r], 0) + 1
        
        return substring_freq == s1_freq

        

