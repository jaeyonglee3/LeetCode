class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, i_val in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -i_val

            l, r = i + 1, len(nums) - 1
            while r > l:
                total = nums[l] + nums[r]

                if total == target:
                    res.append([nums[i], nums[l], nums[r]])

                    while r > l and nums[l] == nums[l + 1]:
                        l += 1
                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
        
        return res