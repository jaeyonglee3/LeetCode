class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = -math.inf
        l, r = 0, len(height) - 1

        while r > l:
            curr_area = min(height[l], height[r]) * (r - l)
            res = max(res, curr_area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return res