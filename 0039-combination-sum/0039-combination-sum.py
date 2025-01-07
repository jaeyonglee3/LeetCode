class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []
        curr_total = 0
        def dfs(i, curr, curr_total):
            if curr_total > target or i > len(candidates) - 1:
                return
            elif curr_total == target:
                res.append(curr[:])
                return 
            
            # Left branch, add a new number
            curr.append(candidates[i])
            curr_total += candidates[i]
            dfs(i, curr, curr_total)

            # Right branch, do not add a new number
            removed = curr.pop()
            curr_total -= removed
            dfs(i + 1, curr, curr_total)
        
        dfs(0, curr, curr_total)

        return res

