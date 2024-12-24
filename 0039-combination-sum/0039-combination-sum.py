class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            elif total > target or i >= len(candidates):
                return
            
            # Include the current candidate i
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            # Remove what we just added
            curr.pop()

            # Do not include the current candidate i
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res