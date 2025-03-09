class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, curr_subset):
            if i > len(nums) - 1:
                res.append(curr_subset.copy())
                return
            
            curr_subset.append(nums[i])
            dfs(i + 1, curr_subset)

            curr_subset.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curr_subset)
        
        dfs(0, [])
        return res