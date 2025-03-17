class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Trivial edge case
        # s2 cannot have a permutation of s1 if s1 is longer
        if len(s1) > len(s2): return False
        
        # Build frequency map for s1 (will not change)
        freq_s1 = Counter(s1)

        # Build frequency map for s2 (changes as window slides over s2)
        freq_s2 = Counter(s2[:len(s1)])
        
        if freq_s1 == freq_s2: return True
        
        # Use fixed sliding window technique to slide over s2
        # left pointer always points to the char to be REMOVED from the window
        # right pointer points to the new char we are adding to our window
        l, r = 0, len(s1)
        while r < len(s2):
            freq_s2[s2[r]] += 1  # Add new char to window
            freq_s2[s2[l]] -= 1  # Remove old char from window
            
            if freq_s2[s2[l]] == 0:
                del freq_s2[s2[l]]  # Remove entry from dict if count becomes 0
            
            # Slide the window along s2
            l += 1
            r += 1

            if freq_s1 == freq_s2: return True
        
        return False

        # time: O(|s2|) since we slide our window over s2 and frequency map updates are O(1)
        # space: O(1) constant b/c freq maps can have at most 26 entries
