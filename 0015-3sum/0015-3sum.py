class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we need 3 numbers x, y, z such that the sum of them is 0
        # let i, j, k be the indices of x, y, z respectively
        
        # 1. sort the input array
        # 2. fix x as one number
        # 3. perform two sum with sorted input array on the remaining part of the arr (target = -x)
        nums.sort()

        res = []
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue

            target = -1 * x

            # perform 2 sum from index i + 1 to the end
            l, r = i + 1, len(nums) - 1
            while r > l:
                y, z = nums[l], nums[r]
                curr_sum = y + z

                if curr_sum == target:
                    res.append([x, y, z])
                    l += 1
                    r -= 1
                    while r > 0 and nums[r] == nums[r + 1]:
                        r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    l += 1
        
        return res

        # [-4, 2, 2, 2, 2]