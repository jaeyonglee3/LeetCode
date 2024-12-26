class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        # iterate through nums twice because it is circular
        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                removed = stack.pop()
                res[removed] = nums[i % n]
            
            if i < n:
                stack.append(i % n)
        
        return res