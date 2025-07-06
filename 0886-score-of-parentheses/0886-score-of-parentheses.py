class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # the stack will only ever include opening parentheses
        stack = []

        for par in s:
            if par == '(':
                stack.append(par)
            else:
                to_multiply = None
                while stack and type(stack[-1]) == int:
                    num = stack.pop()
                    
                    if to_multiply:
                        to_multiply += num
                    else:
                        to_multiply = num
                
                if stack:
                    stack.pop()  # remove the opening bracket that has just been closed
                
                if to_multiply:
                    num = to_multiply * 2
                    stack.append(num)
                else:
                    stack.append(1)

        return sum(stack)
