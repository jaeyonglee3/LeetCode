class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Idea: It's sufficient to compare only adjacent prices because
        # we can make multiple transactions. If the price increases from
        # day i to day i+1, we can effectively simulate buying on day i
        # and selling on day i+1 to capture that profit.
        # This way, we maximize our profit from all upward price movements.

        # i.e. simply capitalizing on every price increase is sufficient to maximize profit
        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        
        return res
