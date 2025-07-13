class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1

        while r >= l:
            if nums[r] ** 2 > nums[l] ** 2:
                res.append(nums[r] ** 2)
                r -= 1
            else:
                res.append(nums[l] ** 2)
                l += 1
        
        res.reverse()
        return res