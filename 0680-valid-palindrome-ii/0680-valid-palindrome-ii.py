class Solution:
    def validPalindrome(self, s: str) -> bool:
        del_used = False
        l, r = 0, len(s) - 1

        def is_palindrome(s):
            l, r = 0, len(s) - 1

            while r >= l:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while r >= l:
            if s[l] != s[r]:
                if r - l == 1:
                    return True
                elif is_palindrome(s[l + 1 : r + 1]) and not del_used:
                    l += 1
                    del_used = True
                elif is_palindrome(s[l : r]) and not del_used:
                    r -= 1
                    del_used = True
                else:
                    return False
            else:
                l += 1
                r -= 1
        
        return True