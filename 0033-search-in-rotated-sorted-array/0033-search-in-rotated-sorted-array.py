# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Goal: O(logn) -> Binary search

        # [4,5,6,7,0,1,2]
        # mid = 7

        # [8, 9, 10, 0, 1, 2, 3, 4, 5]

        # set up l, r ptrs to start at the opposite ends of nums
        # as long as r >= l, calculate a mid index

        # if that mid value is part of the left section
            # if target < mid val and is >= nums[l]: search left of mid
            # otherwise: search right of mid
        # mid value is in the right section
            # if target > mid and is <= nums[r]: search right of mid
            # otherwise: search left of mid
        
        l, r = 0, len(nums) - 1

        while r >= l:
            mid = (l + r) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return mid
            elif mid_val >= nums[0]:
                # we are in the left section
                if target < mid_val and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # we are in the right section
                if target > mid_val and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
