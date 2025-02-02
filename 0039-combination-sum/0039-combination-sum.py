class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, curr_sum):
            if curr_sum == target:
                res.append(subset[:])
                return
            if i >= len(candidates) or curr_sum > target:
                return
            
            # left branch, keep adding i
            # No need for i + 1 because same number can be used multiple times
            subset.append(candidates[i])
            dfs(i, subset, curr_sum + candidates[i])

            # right branch, never include i
            subset.pop()
            dfs(i + 1, subset, curr_sum)
        
        dfs(0, [], 0)
        return res

