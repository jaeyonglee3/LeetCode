class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while r > l:
            curr_area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, curr_area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area        