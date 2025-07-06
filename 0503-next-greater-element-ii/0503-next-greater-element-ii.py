class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # monotonically decreasing (never increasing) stack
        # stack contains (index, num) pairs
        stack = []
        res = [-1] * len(nums)

        for i in range(len(nums) * 2):
            num = nums[i % len(nums)]

            while stack and num > stack[-1][1]:
                removed_i = stack.pop()[0]

                res[removed_i] = num

            if i < len(nums):
                # only add to the stack on the first pass through nums
                stack.append((i, num))
        
        return res