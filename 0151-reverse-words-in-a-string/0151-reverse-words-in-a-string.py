import re

class Solution:
    def reverseWords(self, s: str) -> str:
        # Clean up the string
        s = s.strip()
        s = " " + re.sub(r'\s+', ' ', s)
        word = ""
        res = ""

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                word += s[i]
            else:
                res += word[::-1] + " "
                word = ""
        
        return res[:-1]