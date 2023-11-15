class Solution:
    def longestPalindrome(self, s: str) -> str:
        # variable sized sliding window approach
        # l, r start at index 0
        # while right is still in range
        # if string in window not palindrome or length 1, increment right
        # if string in window is palindrome, increment left, update res
        # res = ""
        # left = right = 0

        # while right <= len(s) - 1:
        #     curr_s = s[left : right + 1]
        #     print(curr_s)

        #     if curr_s != curr_s[::-1] or len(curr_s) == 1:
        #         right += 1
        #     else:
        #         res = curr_s if len(curr_s) > len(res) else res
        #         left += 1
        
        # return res

        if len(s) == 1:
            return s
        
        res = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i : j + 1]
                if substring == substring[::-1]:
                    res = substring if len(substring) > len(res) else res
        
        return res