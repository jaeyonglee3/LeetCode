class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonically decreasing stack problem

        res = [-1] * len(nums1)
        stack = []
        nums1_map = {val : i for i, val in enumerate(nums1)}
        # iterate through nums2 and keep a stack of nums
        # before adding to the stack, check if num being added
        # is greater. If so, we've found stack[-1]'s next greater num.
        # if stack[-1] is in nums1, then res at the same index turns to the difference
        # in the indecies between the curr num2 and stack[-1] in nums2

        for i, num2 in enumerate(nums2):
            # if its greater than value at top of the stack
            # start popping from stack
            while stack and num2 > stack[-1]:
                removed = stack.pop()
                # make res at index of removed element in nums1 equal num2
                # iff nums1 contains the just removed element
                if removed in nums1:
                    res[nums1_map[removed]] = num2
            
            stack.append(num2)
        
        return res