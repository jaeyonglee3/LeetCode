class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # An array is considered balanced if the value of its max element is <= k * min element.
        nums.sort()
        res = 0
        r, l = 0, 0

        while r < len(nums):
            while nums[r] > k * nums[l]:
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return len(nums) - res