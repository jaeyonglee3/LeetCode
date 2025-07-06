class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # monotonically decreasing (never increasing) stack
        # stack contains (index, num) pairs
        stack = []
        res = [-1] * len(nums)

        # do two passes over nums array b/c its circular
        for i in range(len(nums) * 2):
            num = nums[i % len(nums)]

            while stack and num > stack[-1][1]:
                removed = stack.pop()
                removed_i, removed_num = removed[0], removed[1]

                res[removed_i] = num

            if i % len(nums) == i:    
                stack.append((i, num))
        
        return res