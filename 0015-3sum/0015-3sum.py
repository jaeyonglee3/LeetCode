class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # P - return an array of arrays each containing 3 nums that add up to 0 w no duplicates
        # C - 
        # C - how to iterate nums? 
        # L -
        # I - 
        # M -
        # T -

        nums.sort()
        res = []
        seen = set()

        for x_i, x in enumerate(nums):
            # Optimization: Skip duplicate numbers for the fixed 'x'
            # if it isn't the first value in nums
            # and if its the same num as the one before it, skip it!
            if x_i > 0 and nums[x_i] == nums[x_i - 1]:  
                continue 

            target = -x
            # l starts at x_i + 1 because
            l, r = x_i + 1, len(nums) - 1
            
            while r > l:
                curr_sum = nums[l] + nums[r]

                if l == x_i or curr_sum < target:
                    l += 1
                elif r == x_i or curr_sum > target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], x])
                    # e.g. [-2, -2, 0, 0, 2, 2]
                    l += 1
                    while nums[l] == nums[l - 1] and r > l:
                        l += 1
        
        return res