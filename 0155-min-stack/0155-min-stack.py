class MinStack:

    def __init__(self):
        self.stack = []  # stores pairs of numbers, (value, minimum value up to that point in the stack)
        self.min_element = math.inf

    def push(self, val: int) -> None:
        self.min_element = min(self.min_element, val)
        self.stack.append((val, self.min_element))

    def pop(self) -> None:
        self.stack.pop()
        
        if self.stack:
            self.min_element = self.stack[-1][1]
        else:
            self.min_element = math.inf

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()