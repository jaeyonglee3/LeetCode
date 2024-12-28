class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        
        # In the end, the stack will contain the string
        # with the appropriate characters removed

        return "".join(stack)