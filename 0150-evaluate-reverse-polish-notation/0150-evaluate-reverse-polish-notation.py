class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv}
        stack = []

        for token in tokens:
            if token in operators:
                rs = stack.pop()
                ls = stack.pop()
                res = int(operators[token](ls, rs))
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[0]