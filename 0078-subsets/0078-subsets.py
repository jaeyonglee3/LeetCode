class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr_subset):
            if i > len(nums) - 1:
                res.append(curr_subset.copy())
                return
            
            curr_subset.append(nums[i])
            dfs(i + 1, curr_subset)

            curr_subset.pop()
            dfs(i + 1, curr_subset)
        
        dfs(0, [])
        return res
