class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                # c is a closing bracket
                if not stack or stack[-1] not in pairs or pairs[stack[-1]] != c:
                    return False

                stack.pop()
                
        return stack == []
