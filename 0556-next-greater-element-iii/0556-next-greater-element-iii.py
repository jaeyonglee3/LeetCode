class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert n to a list of digits for manipulation
        digits = list(str(n))
        length = len(digits)

        # Step 1: Find the pivot
        # Start from the second last element and move backward to find the 
        # first element which is smaller than its next element
        pivot = -1
        for i in range(length - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pivot = i
                break

        # If no pivot is found, we cannot find a larger permutation
        if pivot == -1:
            return -1

        # Step 2: Find the smallest digit larger than digits[pivot] to its right
        # for i in range(pivot + 1, length):
        for i in range(length - 1, pivot, -1):
            if digits[i] > digits[pivot]:
                digits[i], digits[pivot] = digits[pivot], digits[i]
                break

        # Step 3: Reverse the digits to the right of the pivot to get the smallest arrangement
        digits = digits[:pivot + 1] + sorted(digits[pivot + 1:])

        # Convert back to integer
        res = int("".join(digits))

        # Step 4: Ensure the result is within the 32-bit integer range
        return res if res < (1 << 31) else -1
