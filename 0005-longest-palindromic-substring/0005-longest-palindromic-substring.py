class Solution:
    def longestPalindrome(self, s: str) -> str:
        # to check if any string is a palindrome, we can start from 
        # opposite ends and work towards the middle
        # or we can start from the middle and work outwards 
        # (some middles are two chars if the palindromic string is of even length)
        res_index_start = 0
        longest_len = 0

        for i in range(len(s)):
            # treat every character in the string as 
            # the middle of the potential palindrome
            
            # odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest_len:
                    res_index_start = l
                longest_len = max(longest_len, r - l + 1)
                l -= 1
                r += 1
            
            # even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest_len:
                    res_index_start = l
                longest_len = max(longest_len, r - l + 1)
                l -= 1
                r += 1
        
        return s[res_index_start : res_index_start + longest_len]
