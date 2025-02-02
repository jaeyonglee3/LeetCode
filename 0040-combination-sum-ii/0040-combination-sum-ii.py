class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, subset, curr_sum):
            if curr_sum == target:
                res.append(subset[:])
                return
            if i >= len(candidates) or curr_sum > target:
                return
            
            # left branch, include current candidates[i]
            subset.append(candidates[i])
            dfs(i + 1, subset, curr_sum + candidates[i])

            # right branch, exclude candidates[i] and any duplicates
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            subset.pop()
            dfs(i + 1, subset, curr_sum)
        
        dfs(0, [], 0)
        return res