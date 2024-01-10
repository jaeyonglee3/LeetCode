class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # return [set(nums1) - set(nums2), set(nums2) - set(nums1)]
        return [set(nums1).difference(set(nums2)), set(nums2).difference(set(nums1))]