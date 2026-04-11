class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0

        for customer_account in accounts:
            wealth = sum(customer_account)
            res = max(res, wealth)
        
        return res