class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm):
            # Base case: the permutation contains all the numbers from nums
            # at least once at this point.
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                # if the number is already in the permutation, skip.
                if nums[i] in perm:
                    continue
                
                perm.append(nums[i])
                dfs(perm)
                perm.pop()  # pop from permutation to recursively backtrack
            
            # In Python, if a function reaches the end without an 
            # explicit return statement, it implicitly returns None.
            
        
        dfs([])
        return res