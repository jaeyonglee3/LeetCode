class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = float('-inf')
        l, r = 0, len(height) - 1

        while r > l:
            curr_area = min(height[l], height[r]) * (r - l)
            res = max(curr_area, res)

            # its more favourable to have a taller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res