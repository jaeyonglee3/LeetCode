class MinStack:

    def __init__(self):
        self.stack = []
        self.last_min = math.inf

    def push(self, val: int) -> None:
        self.last_min = min(self.last_min, val)
        self.stack.append((val, self.last_min))
        
    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.last_min = self.stack[-1][1]
        else:
            self.last_min = math.inf

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