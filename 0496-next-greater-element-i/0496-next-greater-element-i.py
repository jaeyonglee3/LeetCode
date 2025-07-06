class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 contains elements from nums2 for which we want to know what the next
        # greater element is from the nums2 list

        # return: an array of size len(nums1) where each element is the next greater value itself

        # subproblem: given nums2 = [1,3,4,2], find the next greater element for each element
        # return: a result array of size len(nums2) where result[i] is the next greater element
        # of nums2[i] if one exists, otherwise is -1

        res = [-1] * len(nums1)
        nums1_indices = {val : i for i, val in enumerate(nums1)}
        nums1 = set(nums1)
        # monotonically decreasing (never increasing) stack
        stack = []

        for i, num in enumerate(nums2):
            while stack and num > stack[-1]:
                # we've found a number that is greater than the number at stack[-1]
                # now, we can update the result
                removed_val = stack.pop()

                if removed_val in nums1:
                    res[nums1_indices[removed_val]] = num
            
            stack.append(num)
        
        return res