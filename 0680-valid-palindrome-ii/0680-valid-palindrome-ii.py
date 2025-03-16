class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while r >= l:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while r >= l:
            if s[r] != s[l]:
                # check if the string can still be a palindrome after
                # remove either s[r] or s[l]
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
            
            l += 1
            r -= 1
        
        return True