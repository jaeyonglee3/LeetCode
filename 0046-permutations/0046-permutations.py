class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr, visited):
            if i > len(nums) - 1:
                res.append(curr[:])
                return
            
            for j in range(len(nums)):
                if visited[j]:
                    continue
                
                curr.append(nums[j])
                visited[j] = True
                dfs(i + 1, curr, visited)

                curr.pop()
                visited[j] = False
        
        dfs(0, [], [False] * len(nums))
        return res
