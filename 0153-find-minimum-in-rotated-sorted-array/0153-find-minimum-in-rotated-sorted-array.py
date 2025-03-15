class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l, r = 0, len(nums) - 1
        while r >= l:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            mid = (r + l) // 2
            curr_val = nums[mid]

            if curr_val < nums[0]:
                # we are in the right sorted portion
                r = mid - 1
                res = curr_val
            else:
                # we are in the left sorted portion
                l = mid + 1

        return res