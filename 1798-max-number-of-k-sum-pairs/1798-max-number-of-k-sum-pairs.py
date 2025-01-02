class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        l, r = 0, len(nums) - 1

        while r > l:
            total = nums[l] + nums[r]

            if total == k:
                res += 1
                l += 1
                r -= 1
            elif total > k:
                r -= 1
            else:
                l += 1
        
        return res