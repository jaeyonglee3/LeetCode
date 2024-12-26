class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # iterate through nums twice b/c its circular

        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(n * 2):
            while stack and nums[i % n] > nums[stack[-1] % n]:
                removed = stack.pop()
                res[removed] = nums[i % n]
            

            # For the first pass, we need to fill the stack with index.
            # Avoid pushing index onto the stack in the second pass to prevent duplicating work.
            if i < n:
                stack.append(i % n)
        
        return res