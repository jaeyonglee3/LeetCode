class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []  # stores indices
        n = len(nums)
        res = [-1] * n

        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                removed = stack.pop()
                res[removed] = nums[i % n]
            
            if i < n:
                stack.append(i)
        
        return res
            
