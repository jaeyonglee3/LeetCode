class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two steps
        # 1. clean up the string (only alnum chars, no uppercase)
        # 2. check if cleaned up string is palindrome (2 pointers)

        clean_s = "".join(c.lower() for c in s if c.isalnum())
        if clean_s == "": return True
        l, r = 0, len(clean_s) - 1

        while r > l:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1
        
        return True