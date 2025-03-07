class StockSpanner:

    def __init__(self):
        self.prices = []  # store (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.prices and self.prices[-1][0] <= price:
            removed = self.prices.pop()
            # notice the span of the current price is always the sum of all the
            # spans belonging to all the prices that are <= the current price.
            span += removed[1]
        
        self.prices.append((price, span))
        return span
             

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)