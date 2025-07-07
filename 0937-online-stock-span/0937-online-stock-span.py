class StockSpanner:

    def __init__(self):
        # monotonically decreasing (never increasing) stack of (price, span) pairs
        self.prices = []

    def next(self, price: int) -> int:
        sum_removed_spans = 0

        while self.prices and self.prices[-1][0] <= price:
            sum_removed_spans += self.prices.pop()[1]
        
        self.prices.append((price, sum_removed_spans + 1))
        return sum_removed_spans + 1
            
             

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# paraphrase
# next(): given today's price p, return the number of days, including today, the stocks price was <= p
# StockSpanner Class: needs to maintain the history of prices in order to calculate the return val of next properly

# dry runs
# (100, 80, 60, 70, 60, 75, 85) <- call next() with all of these
# self.prices = (100, 1), (80, 1), (70, 2), (60, 1)

# approach
# maintain a monotonically decreasing (never increasing) array of prices for the StockSpanner class
# each time a new stock is added, pop from prices to maintain montonic decreasing as necessary
# for all those popped stocks, add up their spans
# use that sum and +1 for the span of the new stock and add that price, span pair to the stack

# implement