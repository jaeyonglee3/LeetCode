class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while r > l:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
        
        return res