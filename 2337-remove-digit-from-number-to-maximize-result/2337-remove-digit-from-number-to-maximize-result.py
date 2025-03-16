class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = -math.inf

        for i, num in enumerate(number):
            if num == digit:
                res = max(res, int(number[:i] + number[i+1:]))

        return str(res)
