class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # the largest squares produced will be the ones furthest from 0
        # either at the far left (negative) or far right (positive)
        # if the square of the number at l ptr is greater than the one at r ptr, swap them
        # only increment the left pointer after a swap. if no swap, keep it there
        # right ptr always moves inwards until it meets the left ptr
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        fill_pos = len(nums) - 1
        
        while r >= l:
            sqr_r, sqr_l = nums[r] ** 2, nums[l] ** 2

            if sqr_r > sqr_l:
                res[fill_pos] = sqr_r
                r -= 1
            else:
                res[fill_pos] = sqr_l
                l += 1
            
            fill_pos -= 1
        
        return res