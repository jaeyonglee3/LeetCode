class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Variable sized fixed window approach
        l = 0
        res = 0
        num_zeros = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1
                
            while num_zeros > 1:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            
            res = max(res, r - l)  # because we must always delete 1 element  
        
        return res
