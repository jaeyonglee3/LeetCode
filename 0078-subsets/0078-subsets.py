class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # i is the index of the value we're making the decision on
        curr_subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr_subset.copy())
                return
            
            # left branch of decision tree
            # decision to include nums[i]
            curr_subset.append(nums[i])
            dfs(i + 1)

            # right branch of decision tree
            # decision NOT to include nums[i]
            curr_subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res