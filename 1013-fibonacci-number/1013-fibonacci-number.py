class Solution:
    def fib(self, n: int) -> int:
        # recursion leafs to repeated calculations
        # and high call stack. iterative is more efficient
        
        # "Base case"
        if n <= 1:
            return n
        
        # keep track only of the last two values
        # O(n) time and O(1) space

        # a, b represent F(0) and F(1)
        a, b = 0, 1
        for _ in range(2, n + 1):
            # "shift" the a and b values
            # b becomes the next fibonacci number
            a, b = b, a + b
        
        # after loop finishes, b holds F(n)
        return b