class Solution:
    def validPalindrome(self, s: str) -> bool:
        # a palindrome is a string that reads the same forwards and backwards

        # s = "abbca"
        # left = b
        # right = c

        # Idea
        # start with two pointers left and right at the start and end of the string
        # move them inwards as long as they point to the same character
        # If we encounter s[left] != s[right]
            # we need to examine whether s[left] or s[right] should be removed
            # substring 1 excludes s[right] = s[left : right]
            # substring 2 excludes s[left] = s[left + 1 : right + 1]
            # if either or both of these two are palindromes, return TRUE
            # if neighter are palindromes, return FALSE
        
        l, r = 0, len(s) - 1

        while r > l:
            if s[l] != s[r]:
                # formulate substrings 1 and 2, check if they're palindromes
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
            
            l += 1
            r -= 1
        
        return True
    
    def isPalindrome(self, s, l, r):
        while r > l:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        
        return True

