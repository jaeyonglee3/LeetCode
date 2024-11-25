import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv, # floordiv b/c division always truncates towards zero
        }
        stack = []
        
        for token in tokens:
            if token in operators.keys():
                rs = stack.pop()
                ls = stack.pop()
                operation = operators[token]
                new_val = operation(ls, rs)
                stack.append(int(math.trunc(new_val)))
            else:
                stack.append(int(token))
        
        return stack[0]
