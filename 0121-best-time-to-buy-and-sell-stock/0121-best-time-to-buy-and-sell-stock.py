class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding window approach
        # Day of buying stock < Day of selling the stock
        # Profit = Sell Price - Buy Price
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            max_profit = max(curr_profit, max_profit)
            
            if curr_profit < 0:
                l = r
            r += 1
        
        return max_profit

