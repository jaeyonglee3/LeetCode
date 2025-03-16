class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_result = ""
        rightmost_index = -1
        n = len(number)

        # new idea: remove the digit where the next digit is greater
        # if none like that exist, remove the rightmost digit

        for i in range(n):
            if number[i] == digit:
                if i != n - 1 and number[i + 1] > number[i]:
                    return number[:i] + number[i + 1 : ]
                else:
                    rightmost_index = i
        
        # there is no place where the digit to remove's next digit
        # is greater than the digit itself
        if rightmost_index == n:
            return number[:n - 1]

        return number[:rightmost_index] + number[rightmost_index + 1 : ]