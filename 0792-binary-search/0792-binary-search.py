class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l, r):
            if not r >= l:
                return -1
            
            mid = (l + r) // 2
            curr_val = nums[mid]

            if curr_val == target:
                return mid
            elif curr_val > target:
                return helper(l, mid - 1)
            else:
                return helper(mid + 1, r)
        
        res = helper(0, len(nums) - 1)
        return res
            
