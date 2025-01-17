class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed sliding window approach
        left, right = 0, len(s1)

        while right <= len(s2):
            substring = s2[left : right]
            if sorted(substring) == sorted(s1):
                return True
            
            left += 1
            right = left + len(s1)
        
        return False