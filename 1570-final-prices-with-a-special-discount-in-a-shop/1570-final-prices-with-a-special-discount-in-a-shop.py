class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []

        for i, price_i in enumerate(prices):
            j = i + 1
            while j < len(prices) and prices[j] > price_i:
                j += 1
            
            if j != len(prices):
                res.append(price_i - prices[j])
            else:
                res.append(price_i)
        
        return res