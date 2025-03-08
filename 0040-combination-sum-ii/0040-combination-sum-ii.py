class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, curr_total):
            if curr_total == target:
                # we create a copy of the subset array at the current point in recursion
                # b/c we use the same subset var across recursive calls and it points
                # to the same address in memory. We create a copy so its not modified
                # by subsequent pops and appends as the recursion continues.
                res.append(subset.copy())
                return
            if i > len(candidates) - 1 or curr_total > target:
                return
            
            # left subtree
            subset.append(candidates[i])
            dfs(i + 1, subset, curr_total + candidates[i])

            # right subtree (check for duplicate i values to skip here)
            subset.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, subset, curr_total)
        
        dfs(0, [], 0)
        return res