class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
      
        while r >= l:
            mid = (l + r) // 2
            curr_val = nums[mid]
            res = min(res, curr_val)
          
            if curr_val > nums[r]:  # Check towards right of curr_val
                l = mid + 1
            elif curr_val < nums[r]:  # Check towards left of curr_val
                r = mid - 1
            else:
                r -= 1  # Handle duplicates by shrinking search space
      
        return res
