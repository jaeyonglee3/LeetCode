class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log n) time + input is sorted = binary search
        res = nums[0]

        if nums[-1] > nums[0]:
            # Then, the entire array is still in ascending order
            # meaning the min element is at the very front
            return res
        
        l, r = 0, len(nums) - 1

        while r >= l:
            mid = (r + l) // 2

            if nums[mid] >= nums[0]:
                # Then, mid is in the LEFT sorted portion
                # The min element is in right half because right half contains all
                # of the smaller elements
                l = mid + 1
            else:
                # Then, mid is in the RIGHT sorted portion
                # result could be nums[mid] or would be to the LEFT of mid b/c
                # anything to the right of mid would be greater than whats currently at mid.
                # to look at left of mid, move right pointer to one beside mid to the left.
                r = mid - 1
                res = nums[mid]
        
        return res