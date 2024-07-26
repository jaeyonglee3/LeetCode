class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solve with a two pointer approach
        clean_s = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(clean_s) - 1

        while r > l:
            if (clean_s[l] != clean_s[r]):
                return False
            
            l += 1
            r -= 1
        
        return True