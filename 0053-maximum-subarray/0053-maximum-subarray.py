class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        curr_sum = 0

        for num in nums:
            curr_sum += num

            if curr_sum > max_sum:
                max_sum = curr_sum
            
            if curr_sum < 0:
                curr_sum = 0  # This "resets" our subarray
        
        return max_sum
            