class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        decomp, closing = [], 0
        left_index = 0

        for i in range(len(s)):
            if s[i] == '(':
                closing += 1
            elif s[i] == ')':
                closing -= 1

            if closing == 0:
                decomp.append(s[left_index + 1 : i])
                left_index = i + 1
        
        return "".join(decomp)
        