class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Approach 1 FAIL: add 1 to the last element. if it is 9, add 1 infront of it
        # digits[-1] = (digits[-1] + 1) % 10
        # if digits[-1] == 0:
        #     digits.insert(-2, 1)
        # return digits

        # Approach 2: Simply convert to an int, add 1, and convert back to an array
        as_int = int(''.join(str(i) for i in digits)) + 1
        return [int(num) for num in str(as_int)]