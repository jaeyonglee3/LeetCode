class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # use a boolean array to keep track of numbers used so far
        visited = [False] * len(nums)

        def dfs(i, perm):
            if i == len(nums):
                res.append(perm.copy())
                return
          
            # Iterate over the nums list to create permutations
            for j in range(len(nums)):
                # Check if the number at index j is already in the current permutation
                if not visited[j]:
                    # Mark it as visited and add to current permutation
                    visited[j] = True
                    perm[i] = nums[j]
                    dfs(i + 1, perm)
                    
                    # Backtrack step: unmark the number at index j as visited for the next iteration
                    visited[j] = False

        dfs(0, [0] * len(nums))
        return res