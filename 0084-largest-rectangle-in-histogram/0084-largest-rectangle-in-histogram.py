class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = -math.inf
        stack = []

        for i, height in enumerate(heights):
            # before adding to stack, check if it is smaller in height
            # than what is currently at the top of the stack

            start = i
            while stack and height < stack[-1][1]:
                # remove from the stack, then calculate the rectangle formed
                removed = stack.pop()
                start = removed[0]
                area = (i - removed[0]) * removed[1]

                res = max(res, area)
            
            stack.append((start, height))
        
        # after traversing the histogram heights,
        # check if the stack still contains anything.
        # anything remaining in the stack can be stretched all the way to the right
        while stack:
            removed = stack.pop()
            area = (len(heights) - removed[0]) * removed[1]
            res = max(res, area)
        
        return res