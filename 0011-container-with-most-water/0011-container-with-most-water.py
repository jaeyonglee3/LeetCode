class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = -math.inf

        while r > l:
            curr_area = (r - l) * min(height[l], height[r])
            res = max(res, curr_area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return res