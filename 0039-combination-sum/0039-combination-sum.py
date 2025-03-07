class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr_subset, curr_total):
            if i > len(candidates) - 1 or curr_total > target:
                return
            if curr_total == target:
                res.append(curr_subset.copy())
                return
            
            curr_subset.append(candidates[i])
            dfs(i, curr_subset, curr_total + candidates[i])

            curr_subset.pop()
            dfs(i + 1, curr_subset, curr_total)
        
        dfs(0, [], 0)
        return res