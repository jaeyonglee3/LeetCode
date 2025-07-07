class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -math.inf
        curr_sum = 0

        for n in nums:
            curr_sum += n
            res = max(res, curr_sum)

            if curr_sum < 0:
                # we must "reset" the curr_sum to start "fresh"
                curr_sum = 0
        
        return res