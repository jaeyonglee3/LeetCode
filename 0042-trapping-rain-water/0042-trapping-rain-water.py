class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while r > l:
            # by working with the pointer with the smaller max value, we retain
            # the min(tallest wall to left or right) part of the equation
            if max_l < max_r:
                res += max(max_l - height[l], 0)
                l += 1
                max_l = max(max_l, height[l])
            else:
                res += max(max_r - height[r], 0)
                r -= 1
                max_r = max(max_r, height[r])
        
        return res