class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')' : '(', '}': '{', ']' : '['}
        stack = []

        for b in s:
            if b in brackets.values():
                stack.append(b)
            else:
                if stack == []: return False
                latest = stack.pop()
                if brackets[b] != latest:
                    return False
        
        return stack == []