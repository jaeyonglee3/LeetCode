class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []

        for c in s:
            if c in brackets.values():
                if not stack:
                    return False

                removed = stack.pop()
                if c != brackets[removed]:
                    return False
            else:
                stack.append(c)
        
        return stack == []