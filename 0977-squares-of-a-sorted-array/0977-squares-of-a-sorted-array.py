class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [n ** 2 for n in nums]
        
        l, r = 0, len(nums) - 1
        res = []

        while r >= l:
            r_squared, l_squared = nums[r] ** 2, nums[l] ** 2

            if r_squared > l_squared:
                res.append(r_squared)
                r -= 1
            else:
                res.append(l_squared)
                l += 1
        
        return list(reversed(res))