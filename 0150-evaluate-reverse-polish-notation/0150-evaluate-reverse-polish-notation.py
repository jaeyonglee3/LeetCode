class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv, # floordiv b/c division always truncates towards zero
        }

        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                operation = operators[token]
                result = operation(left, right)
                stack.append(int(result))
            else:
                stack.append(int(token))
        
        return stack[0]
