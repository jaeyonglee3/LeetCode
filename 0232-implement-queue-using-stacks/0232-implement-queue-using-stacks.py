class MyQueue:

    def __init__(self):
        self.stack1 = []  # for push
        self.stack2 = []  # for pop and peek

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.stack2.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

    def _transfer_if_needed(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
