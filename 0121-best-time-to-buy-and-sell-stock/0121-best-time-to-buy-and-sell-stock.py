class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while r < len(prices) and r > l:
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit, curr_profit)

            if curr_profit < 0:
                l = r
            r += 1
        
        return max_profit