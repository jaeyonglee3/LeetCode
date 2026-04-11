class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        
        for r in range(len(prices)):
            curr_profit = prices[r] - prices[l]
            res = max(res, curr_profit)

            if curr_profit < 0:
                # prices[l] is greater than prices[r]
                l = r
        
        return res