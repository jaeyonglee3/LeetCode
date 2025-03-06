class MinStack:

    def __init__(self):
        self.stack = []
        # last min keeps track of min val at that point in time in the stack
        self.last_min = math.inf

    def push(self, val: int) -> None:
        self.last_min = min(self.last_min, val)
        # append with last_min val so we always know
        # the min val at that point of the stack
        self.stack.append((val, self.last_min))

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.last_min = math.inf
        else:
            # set the last min to the min it was when
            # stack[-1] was at the top of the stack
            # because now its back at the top!
            self.last_min = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.last_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()