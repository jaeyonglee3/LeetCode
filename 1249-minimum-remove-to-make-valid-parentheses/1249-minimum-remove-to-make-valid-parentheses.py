class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid = []
        split_str = list(s)

        for index, c in enumerate(s):
            if c == '(':
                stack.append(index)
            elif c == ')' and stack != []:
                stack.pop()
            elif not c.isalnum():
                invalid.append(index)
        
        if stack != []:
            for p in stack:
                invalid.append(p)

        for i in invalid:
            split_str[i] = ""
        
        return "".join(split_str)