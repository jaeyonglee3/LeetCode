class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed sliding window approach
        size = len(s1)
        left = 0

        while left + size <= len(s2):
            sstring = s2[left: left + size]
            if sorted(sstring) == sorted(s1):
                return True
            
            left += 1
            
        return False