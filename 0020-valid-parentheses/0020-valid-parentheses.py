class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            else:
                # we've encountered a closing parentheses
                removed = stack.pop() if stack else None
                if not removed or pairs[removed] != bracket:
                    return False
        
        return stack == []