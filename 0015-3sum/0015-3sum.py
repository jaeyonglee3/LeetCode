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
            if x_i > 0 and nums[x_i] == nums[x_i - 1]:  
                continue 

            target = -x
            l, r = 0, len(nums) - 1
            
            while r > l:
                curr_sum = nums[l] + nums[r]

                if l == x_i or curr_sum < target:
                    l += 1
                elif r == x_i or curr_sum > target:
                    r -= 1
                else:
                    triple = tuple(sorted([nums[l], nums[r], x]))
                    if triple not in seen:
                        res.append(list(triple))
                        seen.add(triple)
                    l += 1
                    r -= 1
        
        return res