class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        subset = []
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            # All subsets that include nums[i]
            # Left branch, add nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)

            # All subsets that don't include nums[i]
            # Right branch, do not include nums[i]
            # but, be sure to skip any duplicates
            subset.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, subset)
        
        dfs(0, subset)
        return res