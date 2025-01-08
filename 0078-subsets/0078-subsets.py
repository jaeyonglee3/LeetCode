class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            # left branch, add nums[i] to subset
            subset.append(nums[i])
            dfs(i + 1, subset)

            # right branch, do not add nums[i] to subset
            subset.pop()
            dfs(i + 1, subset)
        
        dfs(0, subset)
        return res