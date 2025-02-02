class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            # left branch, includes ALL SUBSETS that include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # right branch, includes all subsets that DO NOT include nums[i]
            # since we cannot include a single nums[i], we need to skip any duplicates of nums[i]
            # here before we make any recursive calls!!
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res