class Solution:
    def isPalindrome(self, s: str) -> bool:
        # More verbose way of getting rid of spaces and non-alphanumeric chars
        # alpha = 'abcdefghijklmnopqrstuvwxyz1234567890'
        # clean_s = ""
        # for c in s.lower():
        #     if c in alpha:
        #         clean_s += c

        clean_s = "".join([c.lower() for c in s if c.isalnum()])
        reverse = clean_s[::-1]
        return reverse == clean_s
        