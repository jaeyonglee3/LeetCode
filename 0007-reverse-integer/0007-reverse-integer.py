class Solution:
    def reverse(self, x: int) -> int:
        # -2^31 and 2^31 - 1
        MIN = -2147483648
        MAX = 2147483647
        
        is_neg = x < 0
        x = abs(x)
        res = 0

        while x != 0:
            digit = x % 10
            x = x // 10

            # Ensure no overflow (no value outside 32-bit integer)
            max_last_digit = MAX % 10  # 7
            min_last_digit = MIN % 10  # 8
            
            if (res > MAX // 10 or res == MAX // 10 and digit >= MAX % 10):
                # result too big
                return 0
            
            # if (res < MIN // 10 or res == MIN // 10 and digit >= MIN % 10):
            #     # result too small
            #     return 0

            # Now, update the digit
            res *= 10
            res += digit
        
        return -1 * res if is_neg else res