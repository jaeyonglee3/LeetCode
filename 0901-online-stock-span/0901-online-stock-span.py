class StockSpanner:

    def __init__(self):
        # use a monotonically decreasing stack
        # (or technically, monotonically non-increasing)
        # of (price, span) pairs.
        # when next is called with price >= stack[-1]
        # keep popping from the stack, adding up the spans for the new price's span
        # this works because spans are transitive, meaning if price A is >= price B,
        # price A's span would include price B's span because B's span is the number
        # of prices <= B, and if a price is <= B, it will also be <= A
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            _, removed_span = self.stack.pop()
            span += removed_span
        
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)