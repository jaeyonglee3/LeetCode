class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = -1

        for i in range(len(number)):
            if number[i] == digit:
                new_num = number[:i] + number[i + 1 : ]

                if int(new_num) > int(res) or res == -1:
                    res = new_num
        
        return res