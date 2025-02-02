class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset[:])  # Append a copy of the subset
                return
            
            # Include nums[i] in the subset (left branch)
            dfs(i + 1, subset + [nums[i]])

            # Exclude nums[i] from the subset (right branch)
            dfs(i + 1, subset)

        dfs(0, [])  # Start DFS with an empty subset
        return res
