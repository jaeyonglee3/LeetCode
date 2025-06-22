class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res, curr_sum = math.inf, 0

        for r in range(len(nums)):
            curr_sum += nums[r]

            if curr_sum >= target:
                while curr_sum >= target:
                    res = min(res, r - l + 1)
                    curr_sum -= nums[l]
                    l += 1
        
        return res if res != math.inf else 0

