class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in perm:
                    continue
                perm.append(nums[i])
                dfs(perm)
                perm.pop()
        
        dfs([])
        return res