class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # greedy solution
        # a key insight is that the result could never be negative, because if all
        # the nums are negative, the subarray w/ the largest sum would be [] which has sum 0
        # so, anytime the curr sum is < 0, reset it back to 0

        res = -math.inf
        curr = 0

        for n in nums:
            curr += n
            res = max(res, curr)

            if curr < 0:
                curr = 0
        
        return res