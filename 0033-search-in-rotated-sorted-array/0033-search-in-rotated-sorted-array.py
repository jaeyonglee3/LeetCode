class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while r >= l:
            mid = (l + r) // 2

            if nums[mid] == target: 
                return mid

            # apply binary search by determining which half of 
            # the array is sorted and whether the target lies within it.
            # Check if left half is sorted
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1