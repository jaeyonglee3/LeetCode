class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the day we buy must come before the day we sell
        # profit = selling price - purchase price

        res = 0

        # left will be the price at which we buy at
        # right will be the selling price
        l, r = 0, 1

        while r <= len(prices) - 1:
            curr_profit = prices[r] - prices[l]
            res = max(curr_profit, res)

            if curr_profit <= 0:
                l = r
            
            r += 1
    
        return res

