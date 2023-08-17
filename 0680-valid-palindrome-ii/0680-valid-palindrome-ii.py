class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Two pointer approach
        p1 = 0
        p2 = len(s) - 1

        while p1 <= p2:
            if s[p1] != s[p2]:
                string1 = s[:p1] + s[p1+1:]  # Try removing mismatched character at p1
                string2 = s[:p2] + s[p2+1:]  # Try removing mismatched character at p2

                # Check if either worked
                return string1 == string1[::-1] or string2 == string2[::-1]
            
            # Increment pointers
            p1 += 1
            p2 -= 1
        
        return True

