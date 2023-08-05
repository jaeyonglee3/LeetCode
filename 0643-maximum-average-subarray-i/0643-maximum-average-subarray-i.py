class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Attempt 1: TLE, list slicing takes too long
        # l_pointer = 0
        # max_avg = -math.inf

        # for r_pointer in range(k - 1, len(nums)):
        #     # avg = sum(nums[l_pointer : r_pointer + 1]) / k
        #     avg = prev_avg - num[l_pointer - 1]
        #     max_avg = max(max_avg, avg)
        #     l_pointer += 1
        
        # return max_avg

        avg = max_avg = sum(nums[:k]) / k

        for i in range(k, len(nums)):
            avg += (nums[i] - nums[i - k]) / k
            max_avg = max(avg, max_avg)
        
        return max_avg