class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = number

        for i in range(len(number)):
            if number[i] == digit:
                new_num = number[:i] + number[i+1:]
                if int(max_num) < int(new_num) or max_num == number:
                    max_num = new_num
        return max_num