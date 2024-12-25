class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonically decreasing stack problem, solves in O(n1 + n2) time
        res = [-1] * len(nums1)
        stack = []
        nums1_map = {val : i for i, val in enumerate(nums1)}

        for i, num2 in enumerate(nums2):
            while stack and num2 > stack[-1]:
                removed = stack.pop()

                # constant time lookup! O(1)
                # instead of O(n1) lookup with "removed in nums1"
                if removed in nums1_map:
                    res[nums1_map[removed]] = num2
            
            stack.append(num2)
        
        return res