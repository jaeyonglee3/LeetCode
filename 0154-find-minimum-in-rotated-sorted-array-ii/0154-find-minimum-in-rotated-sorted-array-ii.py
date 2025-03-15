class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
      
        while r >= l:
            mid = (l + r) // 2
            curr_val = nums[mid]
            res = min(res, curr_val)
          
            if curr_val > nums[r]:
                # Check towards right of curr_val
                # Smaller numbers clearly exist towards the right of curr_val
                l = mid + 1
            elif curr_val < nums[r]:
                # Check towards left of curr_val
                # we've either just visited the min, or there are more values
                # belonging to the right sorted section that we need to check
                r = mid - 1
            else:
                # Handle duplicates by shrinking search space
                # Since we have a duplicate, either curr_value itself is the min value
                # or something else all. What we know for sure is that theres no need to
                # keep nums[r] in the search range/window
                r -= 1  
      
        return res
