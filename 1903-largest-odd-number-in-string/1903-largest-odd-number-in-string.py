class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Any number that ends with an odd digit is an odd number. 
        # If a digit in num is an odd number, then 
        # the substring from index 0 to the current digit is the largest odd number that ends with the digit. 
        # We can simply find the rightmost odd digit in nums, and 
        # return the substring from index 0 to the rightmost odd digit.
        
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:  
                return num[:i + 1]
        
        return ""
