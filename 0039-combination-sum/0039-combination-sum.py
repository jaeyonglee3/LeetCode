class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr_nums, curr_sum):
            if curr_sum == target:
                res.append(curr_nums[:])
                return
            if i > len(candidates) - 1 or curr_sum > target:
                return
            
            # left branch
            curr_nums.append(candidates[i])
            dfs(i, curr_nums, curr_sum + candidates[i])

            # right branch
            curr_nums.pop()
            dfs(i + 1, curr_nums, curr_sum)

        dfs(0, [], 0)
        return res

