class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # the largest squares produced will be the ones furthest from 0
        # either at the far left (negative) or far right (positive)
        # construct a result list by filling it in backwards
        # populate result with the greater between the two squares at either ptr
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