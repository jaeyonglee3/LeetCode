class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if abs(target - total) < abs(target - res):
                    # if the difference between target and current total is less than
                    # the difference between target and result, update result
                    res = total

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    # exact match, just return the target
                    return target

        return res
