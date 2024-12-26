class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i):
            if i == len(nums):
                # the permutation contains all elements
                # we have a complete permutation we can add to results
                res.append(curr[:])
                return
            
            for j in range(len(nums)):
                if not visited[j]:
                    curr[i] = nums[j]
                    visited[j] = True
                    dfs(i + 1)
                    visited[j] = False
        
        len_nums = len(nums)  # Store the length of the input list
        visited = [False] * len_nums  # Create a visited list to track numbers that are used
        curr = [0] * len_nums  # Temp list to store the current permutation
        
        dfs(0)  # Start generating permutations from index 0
        return res