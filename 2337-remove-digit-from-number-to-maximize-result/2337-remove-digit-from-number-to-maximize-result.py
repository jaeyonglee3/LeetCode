class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_result = ""

        for i in range(len(number)):
            if number[i] == digit:
                # Create a new number by removing the digit at index i
                new_number = number[:i] + number[i+1:]
                # Update max_result if the new number is greater
                if new_number > max_result:
                    max_result = new_number

        return max_result
