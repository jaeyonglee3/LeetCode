class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while r > l:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)

            # move the pointer that has the smaller height
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return res