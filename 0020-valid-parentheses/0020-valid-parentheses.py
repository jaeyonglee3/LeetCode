class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []

        for char in s:
            if char in pairs:
                # char is an opening bracket
                stack.append(char)
            else:
                # char is not an opening bracket
                if stack:
                    removed = stack.pop()
                    if pairs[removed] != char:
                        return False
                else:
                    return False
        
        return stack == []
