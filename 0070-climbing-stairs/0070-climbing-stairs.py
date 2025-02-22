class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.dfs(n, memo)
    
    def dfs(self, n, memo):
        if n == 0 or n == 1:
            return 1
        
        if n not in memo:
            memo[n] = self.dfs(n-1, memo) + self.dfs(n-2, memo)
        
        return memo[n]
