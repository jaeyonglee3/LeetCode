class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort candidates arr to ensure all duplicates are consecutive 
        candidates.sort()

        def dfs(i, curr, curr_total):
            if curr_total == target:
                res.append(curr[:])
                return
            if i > len(candidates) - 1 or curr_total > target:
                return
            
            # Left branch, include candidates[i]
            curr.append(candidates[i])
            curr_total += candidates[i]
            dfs(i + 1, curr, curr_total) # call with i+1 to avoid reusing the same element twice

            # Right branch, skip candidates[i]
            removed = curr.pop()
            curr_total -= removed

            while i != len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                # Move i to the very last duplicated value
                # Duplicates will be consecutive since we sorted candidates arr
                i += 1
            dfs(i + 1, curr, curr_total)
        
        dfs(0, [], 0)
        return res