class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = max_len = 0
        zeroes = ones = 0

        if 0 not in nums:
            return len(nums) - 1

        # for r, num in enumerate(nums):
        #     if not num and not deleted:
        #         max_len = max(max_len, r - l + 1)
        #         deleted = True
        #     elif not num:
        #         max_len = max(max_len, r - l - 1)
        #         l += 1

        for r, num in enumerate(nums):
            if num == 0:
                zeroes += 1
                while zeroes > 1:  # if there are >1 zeroes, shift left pointer until only 1 zero left in subarray
                    if nums[l] == 0:
                        zeroes -= 1
                    else:
                        ones -= 1
                    l += 1
            else:
                ones += 1
            
            max_len = max(max_len, ones)
        
        return max_len if zeroes == 1 else max_len - 1