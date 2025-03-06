class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv}

        for token in tokens:
            if token in operators:
                rs = stack.pop()
                ls = stack.pop()
                result = int(operators[token](ls, rs))
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]