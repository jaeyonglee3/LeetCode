class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonically decreasing stack problem, solves in O(n1 + n2) time
        res = [-1] * len(nums1)
        stack = []
        next_greater = {}

        for i, num2 in enumerate(nums2):
            while stack and num2 > stack[-1]:
                removed = stack.pop()
                next_greater[removed] = num2
            
            stack.append(num2)
        
        return [next_greater.get(num, -1) for num in nums1]