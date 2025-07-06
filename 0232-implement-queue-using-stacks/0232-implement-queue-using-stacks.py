class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        # move everything in stack1 to stack2
        # pop from stack2 and return
        # then, pop from stack2 until its empty to return everything back to stack1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        popped_val = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        return popped_val

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        popped_val = self.stack2.pop()
        self.stack1.append(popped_val)

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        return popped_val

    def empty(self) -> bool:
        return self.stack1 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()