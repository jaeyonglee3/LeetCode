class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]:
                print(a)
                continue
            
            target2 = target - nums[a]

            for b in range(a + 1, len(nums)):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                # look for 3 numbers that sum to target2
                target3 = target2 - nums[b]

                # look for 2 numbers that sum to target3
                l, r = b + 1, len(nums) - 1

                while r > l:
                    total = nums[r] + nums[l]
                    if total == target3:
                        res.append([nums[a], nums[b], nums[l], nums[r]])

                        while r > l and nums[l] == nums[l + 1]:
                            l += 1
                        while r > l and nums[r] == nums[r - 1]:
                            r -= 1
                        
                        l += 1
                        r -= 1
                    elif total > target3:
                        r -= 1
                    else:
                        l += 1
        return res
