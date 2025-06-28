class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Variable sized fixed window approach
        l = 0
        res = 0
        flip_used = False

        for r in range(len(nums)):
            if nums[r] == 0 and not flip_used:
                flip_used = True
            elif nums[r] == 0 and flip_used:
                advance_l = True
                
                while advance_l:
                    if nums[l] == 0:
                        advance_l = False
                    l += 1
            
            curr_len = r - l if flip_used else r - l + 1
            res = max(res, curr_len)
        
        return res - 1 if not flip_used else res
