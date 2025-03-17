class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        # Build frequency map for s1        
        freq_s1 = {}
        for c in s1:
            freq_s1[c] = freq_s1.get(c, 0) + 1

        # Build frequency map for s2
        freq_s2 = {}
        for c in s2[:len(s1)]:
            freq_s2[c] = freq_s2.get(c, 0) + 1
        
        if freq_s1 == freq_s2: return True
        
        # Use fixed sliding window technique to slide over s2
        l, r = 0, len(s1)
        while r < len(s2):
            freq_s2[s2[r]] = freq_s2.get(s2[r], 0) + 1  # Add new char to window
            freq_s2[s2[l]] = freq_s2.get(s2[l], 0) - 1  # Remove old char from window
            
            if freq_s2[s2[l]] == 0:
                del freq_s2[s2[l]]  # Remove key if count becomes 0
            
            # slide the window
            l += 1
            r += 1

            if freq_s1 == freq_s2: return True
        
        return False
