class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        freq_s1 = Counter(s1)
        freq_s2 = Counter(s2[:len(s1)])
        
        if freq_s1 == freq_s2: return True
        
        l, r = 0, len(s1)
        while r < len(s2):
            freq_s2[s2[r]] += 1  # Add new char to window
            freq_s2[s2[l]] -= 1  # Remove old char from window
            
            if freq_s2[s2[l]] == 0:
                del freq_s2[s2[l]]  # Remove key if count becomes 0
            
            # slide the window
            l += 1
            r += 1

            if freq_s1 == freq_s2: return True
        
        return False
