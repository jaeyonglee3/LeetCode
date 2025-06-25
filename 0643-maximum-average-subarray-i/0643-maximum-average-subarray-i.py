class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k - 1
        max_sum = curr_sum = sum(nums[0 : k])

        while r < len(nums):
            curr_sum -= nums[l]

            # slide the window over
            l += 1
            r += 1

            if r < len(nums):
                curr_sum += nums[r]
                max_sum = max(max_sum, curr_sum)
        
        return max_sum / k