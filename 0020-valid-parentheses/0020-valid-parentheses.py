class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif s[i] == ')' and stack[-1] != '(':
                    return False
                elif s[i] == '}' and stack[-1] != '{':
                    return False
                elif s[i] == ']' and stack[-1] != '[':
                    return False
                else:
                    stack.pop()

        return stack == []

