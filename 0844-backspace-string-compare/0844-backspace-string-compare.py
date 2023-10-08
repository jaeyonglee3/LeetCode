class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        typed_s = typed_t = ""

        for c in s:
            if c != "#":
                typed_s += c
            else:
                typed_s = typed_s[:len(typed_s) - 1]
        
        for c in t:
            if c != "#":
                typed_t += c
            else:
                typed_t = typed_t[:len(typed_t) - 1]
        
        return typed_s == typed_t
        