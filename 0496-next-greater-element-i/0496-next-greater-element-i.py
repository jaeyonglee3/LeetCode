class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        num1_map = {n : i for i, n in enumerate(nums1)}
        stack = []

        for n in nums2:
            while stack and stack[-1] < n:
                removed = stack.pop()
                if removed in num1_map:
                    ans[num1_map[removed]] = n
            
            stack.append(n)
        
        return ans