class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # naive sol'n: triple nested for loops, but cannot avoid duplicates 
        res = []
        nums.sort()

        for i, val in enumerate(nums): 
            # dont want to reuse same value in same position twice
            if i > 0 and val == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = val + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res