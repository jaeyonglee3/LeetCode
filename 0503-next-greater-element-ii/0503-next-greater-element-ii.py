class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # iterate through nums twice b/c its circular

        n = len(nums)
        res = [-1] * n
        stack = []
        nums_map = {val : i for i, val in enumerate(nums)}

        for i in range(n * 2):
            while stack and nums[i % n] > nums[stack[-1] % n]:
                removed = stack.pop() % n
                res[removed] = nums[i % n]
            
            stack.append(i)
        
        return res