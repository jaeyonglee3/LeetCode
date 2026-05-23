class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = -math.inf

        while r > l:
            curr_amount = min(height[l], height[r]) * (r - l)
            res = max(res, curr_amount)

            # move the pointer pointing to the shorter bar
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return res