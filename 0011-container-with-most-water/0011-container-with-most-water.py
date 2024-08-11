class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while r > l:
            smaller = min(height[l], height[r])
            curr_area = smaller * (r - l)
            if curr_area > res:
                res = curr_area
            
            if height[r] == smaller:
                r -= 1
            else:
                l += 1
        
        return res