class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set()
        for num in nums1:
            nums1_set.add(num)
        
        res = set()
        for num in nums2:
            if num in nums1_set and num not in res:
                res.add(num)

        return list(res)