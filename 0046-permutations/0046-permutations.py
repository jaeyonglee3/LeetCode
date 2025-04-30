class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        def dfs(i, curr_perm):
            if i == len(nums):
                res.append(curr_perm.copy())
                return
            
            for j in range(len(nums)):
                if visited[j]:
                    continue
                
                visited[j] = True
                curr_perm[i] = nums[j]
                dfs(i + 1, curr_perm)
                visited[j] = False

        
        dfs(0, [0] * len(nums))
        return res