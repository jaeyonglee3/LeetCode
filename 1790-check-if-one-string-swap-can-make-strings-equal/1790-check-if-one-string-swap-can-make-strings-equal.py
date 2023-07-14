class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if sorted(s1) == sorted(s2):        
            swap_count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i] and s1[i] in s2:
                    swap_count += 1
            
            return (swap_count == 2)

        return False

        # edge case: what if there are exactly two diff chars and len of s1 is 3?
        # act
        # bcp
        # attack
        # defend
