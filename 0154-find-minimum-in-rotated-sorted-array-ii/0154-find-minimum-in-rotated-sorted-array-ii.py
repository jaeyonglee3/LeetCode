class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]  # Initialize res with the first element
      
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])  # Update res with the current minimum value
          
            if nums[mid] > nums[r]:  # Minimum is in the right half
                l = mid + 1
            elif nums[mid] < nums[r]:  # Minimum is in the left half
                r = mid - 1
            else:
                r -= 1  # Handle duplicates by shrinking search space
      
        return res  # Return the tracked minimum value
