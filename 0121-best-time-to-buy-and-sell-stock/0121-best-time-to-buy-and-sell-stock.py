class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0  # represents the price we buy it for

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            res = max(res, profit)

            if profit < 0:
                l = r
        
        return res