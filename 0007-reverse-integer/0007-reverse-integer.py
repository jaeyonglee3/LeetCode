class Solution:
    def reverse(self, x: int) -> int:
        # -2^31 and 2^31 - 1

        str_x = str(x)
        if x < 0:
            str_x = str_x[1: ]
        
        str_x = str_x[::-1]
        result = int(str_x)

        if x < 0:
            result *= -1
        
        if result < -1 * (2 ** 31) or result > (2 ** 31) + 1:
            return 0
        
        return result