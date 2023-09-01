class Solution:
    def mySqrt(self, x: int) -> int:
        # find the largest k such that k^2 <= x
        # set right = x + 1 instead of right = x to deal with 
        # special input cases like x = 0 and x = 1.

        left, right = 0, x + 1

        while left < right:
            mid = (right + left) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid + 1
        
        return left - 1