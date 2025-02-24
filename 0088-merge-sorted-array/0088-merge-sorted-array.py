class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_ptr = m + n - 1
        ptr1, ptr2 = m - 1, n - 1

        # Merge in reverse order
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[insert_ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[insert_ptr] = nums2[ptr2]
                ptr2 -= 1
            
            insert_ptr -= 1
        
        # Edge case: nums1: [20, 0, 0, 0] and nums2: [1, 2, 3]
        # ptr1 becomes negative while there are remaining elements
        # in nums2 array. we must fill nums1 with the left over
        # elements from nums2.
        while ptr2 >= 0:
            nums1[insert_ptr] = nums2[ptr2]
            ptr2 -= 1
            insert_ptr -= 1
    