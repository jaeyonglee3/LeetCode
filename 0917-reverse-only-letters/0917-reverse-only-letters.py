class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        mapping = {}
        clean = ""

        for idx, char in enumerate(s):
            if not char.isalpha():
                mapping[idx] = char
            else:
                clean += char
        
        clean = clean[::-1]

        for idx in mapping:
            clean = clean[:idx] + mapping[idx] + clean[idx:]
        
        return clean