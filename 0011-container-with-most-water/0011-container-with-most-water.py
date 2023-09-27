class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE TLE, O(n^2)
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i, len(height)):
        #         h = min(height[i], height[j])
        #         width = j - i
        #         area = h * width
        #         max_area = max(max_area, area)
        
        # return max_area

        max_area = 0
        l, r = 0, len(height) - 1  # initialize with max possible width
        # calculate area each time
        # increment/decrement the pointer with the shorter height
        # stop when l < r is false
        # O(n) runtime

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        
        return max_area

