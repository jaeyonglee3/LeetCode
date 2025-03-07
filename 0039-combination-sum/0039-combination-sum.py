class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr_combo, curr_total):
            if i > len(candidates) - 1 or curr_total > target:
                return
            if curr_total == target:
                res.append(curr_combo.copy())
                return
            
            # left branch
            curr_combo.append(candidates[i])
            dfs(i, curr_combo, curr_total + candidates[i])

            # right branch
            curr_combo.pop()
            dfs(i + 1, curr_combo, curr_total)
        
        dfs(0, [], 0)
        return res