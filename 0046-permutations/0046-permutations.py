class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        def dfs(i, curr):
            if i > len(nums) - 1:
                res.append(curr[:])
                return
            
            for j in range(len(nums)):
                if visited[j]:
                    continue
                
                curr.append(nums[j])
                visited[j] = True
                dfs(i + 1, curr)

                curr.pop()
                visited[j] = False
        
        dfs(0, [])
        return res
