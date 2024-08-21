class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_total = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit_total += prices[i] - prices[i - 1]
        
        return profit_total


        