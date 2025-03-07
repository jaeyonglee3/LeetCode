class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices.copy()
        stack = []  # monotonically increasing stack storing (index, price)

        for i, price_i in enumerate(prices):
            while stack and stack[-1][1] >= price_i:
                removed = stack.pop()
                res[removed[0]] = removed[1] - price_i
            
            stack.append((i, price_i))
        
        return res