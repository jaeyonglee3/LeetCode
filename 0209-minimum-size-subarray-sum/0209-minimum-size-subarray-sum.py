class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res, curr_sum = math.inf, nums[l]

        while r < len(nums):
            if curr_sum >= target:
                while curr_sum >= target:
                    res = min(res, r - l + 1)
                    curr_sum -= nums[l]
                    l += 1
            else:
                r += 1
                curr_sum += nums[r] if r < len(nums) else 0
        
        return 0 if res == math.inf else res