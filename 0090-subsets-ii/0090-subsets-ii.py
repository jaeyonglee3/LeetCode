class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            # Left branch, add nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Right branch, do not include nums[i]
            # but, be sure to skip any duplicates
            subset.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        
        dfs(0)
        return res