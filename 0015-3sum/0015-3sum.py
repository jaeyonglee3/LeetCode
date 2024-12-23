class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, i_val in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            # Optimization: Skip duplicate numbers for the fixed 'x'
            # if it isn't the first value in nums
            # and if its the same num as the one before it, skip it!
            if i > 0 and i_val == nums[i - 1]:  
                continue 

            while r > l:
                curr_sum = nums[l] + nums[r]
                
                if curr_sum == -i_val:
                    res.append([i_val, nums[r], nums[l]])
                    # e.g. [0, -2, -2, 0, 0, 2, 2]
                    # Optimization: Skip duplicate numbers for 'l' and 'r'
                    # Because its sorted, all duplicates would be next to each other!
                    while l < r and nums[l] == nums[l + 1]:  
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif curr_sum > -i_val:
                    r -= 1
                else:
                    l += 1
        
        return res





