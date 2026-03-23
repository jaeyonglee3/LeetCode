class MinStack:

    def __init__(self):
        # stack stores the item and min item at the time of push
        # (item, curr_min)
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append((val, val))
        else:
            curr_min = self.stack[-1][1]
            self.stack.append((val, min(val, curr_min)))

    def pop(self) -> None:
        self.stack.pop()

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