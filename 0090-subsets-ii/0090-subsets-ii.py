class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return            
            
            # Left branch, add nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # right brach, do not add nums[i]
            subset.pop()
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1)
        
        dfs(0)
        return res